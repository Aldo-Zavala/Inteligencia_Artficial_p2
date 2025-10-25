from itertools import product

# --- Modelo: dominios ---
disease_vals = [True, False]          # Disease = {True, False}
test_vals    = ['Pos', 'Neg']         # Test = {Pos, Neg}
action_vals  = ['Treat', 'NoTreat']   # Decision actions

# --- Parámetros (ejemplo) ---
P_disease = {True: 0.1, False: 0.9}   # prior P(Disease)

# P(Test | Disease)
# sensibilidad y especificidad ejemplo:
# P(Test=Pos | Disease=True) = 0.9  (sensibilidad)
# P(Test=Pos | Disease=False) = 0.2 (falsos positivos)
P_test_given_d = {
    True:  {'Pos': 0.9, 'Neg': 0.1},
    False: {'Pos': 0.2, 'Neg': 0.8}
}

# Utility function U(action, disease)
# ejemplo:
# - Si tratamos y hay enfermedad: utilidad alta (curamos) pero con coste tratamiento
# - Si tratamos y no hay enfermedad: coste del tratamiento (negativo)
# - Si no tratamos y hay enfermedad: utilidad muy negativa por no tratar
# - Si no tratamos y no hay enfermedad: utilidad 0
U = {
    ('Treat', True):   80,   # beneficio neto si tratamos y hay enfermedad
    ('Treat', False): -10,   # coste de tratar a sano
    ('NoTreat', True): -200, # daño por no tratar enfermedad
    ('NoTreat', False): 0    # nada pasa
}

# --- Funciones auxiliares ---
def joint_prob_d_and_test(d, t):
    """P(D=d, Test=t) = P(D=d) * P(Test=t | D=d)"""
    return P_disease[d] * P_test_given_d[d][t]

def marginal_prob_test(t):
    """P(Test=t) = sum_d P(D=d)P(Test=t|D=d)"""
    return sum(joint_prob_d_and_test(d, t) for d in disease_vals)

def posterior_d_given_test(d, t):
    """P(D=d | Test=t) = P(D=d, Test=t)/P(Test=t)"""
    p_joint = joint_prob_d_and_test(d, t)
    p_t = marginal_prob_test(t)
    return p_joint / p_t if p_t > 0 else 0.0

# --- Evaluación de una política ---
# Política: dict mapping test_val -> action (e.g. {'Pos':'Treat', 'Neg':'NoTreat'})
def expected_utility_of_policy(policy):
    """
    EU(policy) = sum_{t} P(Test=t) * [ sum_{d} P(d|t) * U(policy(t), d) ]
    """
    eu = 0.0
    for t in test_vals:
        p_t = marginal_prob_test(t)
        if p_t == 0:
            continue
        action = policy[t]
        # Esperanza condicional de utilidad dada la observación t
        eu_cond = sum(posterior_d_given_test(d, t) * U[(action, d)] for d in disease_vals)
        eu += p_t * eu_cond
    return eu

# --- Enumerar políticas deterministas y encontrar la óptima ---
def find_optimal_policy():
    best_policy = None
    best_eu = -float('inf')
    # todas las asignaciones test_vals -> action_vals
    for actions in product(action_vals, repeat=len(test_vals)):
        policy = dict(zip(test_vals, actions))
        eu = expected_utility_of_policy(policy)
        if eu > best_eu:
            best_eu = eu
            best_policy = policy
    return best_policy, best_eu

# --- Ejecutar ejemplo ---
if __name__ == "__main__":
    best_policy, best_eu = find_optimal_policy()
    print("Política óptima (map Test->Action):", best_policy)
    print("Utilidad esperada de la política óptima:", best_eu)

    # Mostrar EU de todas las políticas para comparar
    print("\nTodas las políticas (EU):")
    for actions in product(action_vals, repeat=len(test_vals)):
        policy = dict(zip(test_vals, actions))
        print(policy, "EU =", expected_utility_of_policy(policy))
