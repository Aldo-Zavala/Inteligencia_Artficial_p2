import itertools

# --------------------------------------
# Juego base: Dilema del prisionero
# --------------------------------------
# Estrategias: Cooperar (C) o Traicionar (D)
players = ['A', 'B']
strategies = ['C', 'D']

# Pagos: (A, B)
# Formato: payoff[(estrategiaA, estrategiaB)] = (utilidadA, utilidadB)
payoff = {
    ('C', 'C'): (3, 3),
    ('C', 'D'): (0, 5),
    ('D', 'C'): (5, 0),
    ('D', 'D'): (1, 1),
}

# --------------------------------------
# Función para encontrar equilibrios de Nash puros
# --------------------------------------
def find_nash_equilibria(payoff, strategies):
    nash_eq = []
    for sA, sB in itertools.product(strategies, repeat=2):
        a_payoff = payoff[(sA, sB)][0]
        b_payoff = payoff[(sA, sB)][1]

        # Verifica si A podría mejorar cambiando solo su acción
        best_response_A = max(payoff[(a_alt, sB)][0] for a_alt in strategies)
        best_response_B = max(payoff[(sA, b_alt)][1] for b_alt in strategies)

        if a_payoff == best_response_A and b_payoff == best_response_B:
            nash_eq.append((sA, sB))
    return nash_eq

# --------------------------------------
# Juego original
# --------------------------------------
print("Juego base (Dilema del Prisionero):")
for k, v in payoff.items():
    print(f"{k}: {v}")

eq_base = find_nash_equilibria(payoff, strategies)
print("\nEquilibrio(s) de Nash (juego base):", eq_base)

# --------------------------------------
# Mecanismo de incentivo: el gobierno premia cooperación mutua con +1
# --------------------------------------
payoff_mechanism = {}
for (sA, sB), (uA, uB) in payoff.items():
    if (sA, sB) == ('C', 'C'):
        payoff_mechanism[(sA, sB)] = (uA + 1, uB + 1)  # incentivo a cooperar
    else:
        payoff_mechanism[(sA, sB)] = (uA, uB)

print("\nJuego con mecanismo de incentivo (premio a cooperación):")
for k, v in payoff_mechanism.items():
    print(f"{k}: {v}")

eq_mech = find_nash_equilibria(payoff_mechanism, strategies)
print("\nEquilibrio(s) de Nash con mecanismo:", eq_mech)
