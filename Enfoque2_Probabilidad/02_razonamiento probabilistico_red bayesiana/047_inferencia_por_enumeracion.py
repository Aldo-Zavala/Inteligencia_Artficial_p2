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

# Inferencia por enumeración: P(L|C=1)
numerador = 0
denominador = 0
for L in [0,1]:
    for R in [0,1]:
        joint = P_L[L] * P_R[R] * P_C_given[(L,R)]
        if L==1:
            numerador += joint
        denominador += joint

P_L_given_C = numerador / denominador
print(f"P(Lluvia=1 | Calle mojada) = {P_L_given_C:.3f}")
