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

# Muestreo directo por rechazo
n_samples = 10000
accepted = []
for _ in range(n_samples):
    # Generar L y R según su prior
    L = 1 if random.random() < P_L[1] else 0
    R = 1 if random.random() < P_R[1] else 0
    # Generar C según P(C|L,R)
    C = 1 if random.random() < P_C_given[(L,R)] else 0
    # Rechazar si C != evidencia (C=1)
    if C == 1:
        accepted.append(L)

# Estimar P(L=1 | C=1)
P_L_given_C = sum(accepted)/len(accepted)
print(f"P(Lluvia=1 | Calle mojada) ≈ {P_L_given_C:.3f}")
