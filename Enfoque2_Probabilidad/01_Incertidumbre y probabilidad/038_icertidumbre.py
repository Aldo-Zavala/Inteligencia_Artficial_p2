import random

# GridWorld 1x3 (simplificado)
world = [0, 0, +1]

# Probabilidades de transición
trans_prob = 0.8  # éxito al moverse
gamma = 0.9
V = [0, 0, 0]

# Actualización iterativa de valores
for _ in range(100):
    V_new = V.copy()
    for s in range(2):  # no incluimos la meta
        # Esperanza de utilidad considerando incertidumbre
        EU = trans_prob*(1 + gamma*V[s+1]) + (1-trans_prob)*(0 + gamma*V[s])
        V_new[s] = EU
    V = V_new

print("Valores de estado bajo incertidumbre:")
print(V)

# Política óptima
policy = []
for s in range(2):
    EU_move = trans_prob*(1 + gamma*V[s+1]) + (1-trans_prob)*(0 + gamma*V[s])
    EU_stay = 0 + gamma*V[s]
    policy.append("Derecha" if EU_move >= EU_stay else "Quedarse")

print("Política óptima considerando incertidumbre:")
print(policy)
