# P(A) = lluvia
P_A = 0.3

# P(C) = sistema de riego
P_C = 0.5

# P(B | A, C) = calle mojada dado lluvia y riego
P_B_given_A_C = {
    (1,1): 0.99,  # lluvia y riego
    (1,0): 0.9,   # lluvia sin riego
    (0,1): 0.8,   # no lluvia pero riego
    (0,0): 0.1    # ni lluvia ni riego
}

# Independencia condicional: P(A | B, C) = P(A | C)
# Ejemplo: C = sistema de riego activo (C=1)
C = 1
# Sin considerar B, P(A|C)
# Aquí simplemente mostramos el concepto:
P_A_given_C = 0.3  # supongamos que la probabilidad de lluvia no cambia al saber riego

print(f"P(A|C=1) = {P_A_given_C}")
print("Según independencia condicional, P(A|B,C) = P(A|C) = ", P_A_given_C)
