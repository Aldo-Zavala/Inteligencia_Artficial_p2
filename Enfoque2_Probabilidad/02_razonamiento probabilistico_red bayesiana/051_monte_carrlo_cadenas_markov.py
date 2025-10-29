import random

# Priors
P_L = {0:0.7, 1:0.3}
P_R = {0:0.6, 1:0.4}
P_C_given = {
    (0,0): 0.0,
    (0,1): 0.8,
    (1,0): 0.9,
    (1,1): 0.99
}

# Gibbs Sampling
n_samples = 10000
samples = []
# Estado inicial
L, R, C = 0, 0, 1  # C=1 evidencia

for _ in range(n_samples):
    # Muestrear L dado R y C
    prob_L = P_L[1]*P_C_given[(1,R)] / (P_L[0]*P_C_given[(0,R)] + P_L[1]*P_C_given[(1,R)])
    L = 1 if random.random() < prob_L else 0
    
    # Muestrear R dado L y C
    prob_R = P_R[1]*P_C_given[(L,1)] / (P_R[0]*P_C_given[(L,0)] + P_R[1]*P_C_given[(L,1)])
    R = 1 if random.random() < prob_R else 0
    
    # C está fijado por evidencia C=1
    samples.append(L)

# Estimar P(L=1 | C=1)
P_L_given_C = sum(samples)/len(samples)
print(f"P(Lluvia=1 | Calle mojada) ≈ {P_L_given_C:.3f}")
