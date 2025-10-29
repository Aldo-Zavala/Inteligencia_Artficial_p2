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

# Eliminación de la variable oculta R
factor = {}
for L in [0,1]:
    suma = 0
    for R in [0,1]:
        suma += P_C_given[(L,R)] * P_R[R]
    factor[L] = suma * P_L[L]

# Normalizar
Z = sum(factor.values())
P_L_given_C = {L: factor[L]/Z for L in factor}
print("P(Lluvia | Calle mojada) =", P_L_given_C)
