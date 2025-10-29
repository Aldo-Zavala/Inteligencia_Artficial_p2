import random

# Priors
P_L = {0:0.7, 1:0.3}
P_R = {0:0.6, 1:0.4}

# P(C|L,R)
P_C_given = {
    (0,0): 0.0,
    (0,1): 0.8,
    (1,0): 0.9,
    (1,1): 0.99
}

# Ponderación de verosimilitud
n_samples = 10000
weights = {0:0.0, 1:0.0}

for _ in range(n_samples):
    # Generar L y R
    L = 1 if random.random() < P_L[1] else 0
    R = 1 if random.random() < P_R[1] else 0
    # Peso según evidencia C=1
    w = P_C_given[(L,R)]
    # Acumular peso según valor de L
    weights[L] += w

# Normalizar
total = weights[0] + weights[1]
P_L_given_C = {L: weights[L]/total for L in weights}
print(f"P(Lluvia=1 | Calle mojada) ≈ {P_L_given_C[1]:.3f}")
