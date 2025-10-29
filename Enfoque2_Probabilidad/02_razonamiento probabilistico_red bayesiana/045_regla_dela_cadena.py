# Probabilidades individuales
P_Lluvia = 0.3
P_Riego = 0.5

# Probabilidad condicional P(Calle | Lluvia, Riego)
P_Calle_given = {
    (1,1): 0.99,
    (1,0): 0.9,
    (0,1): 0.8,
    (0,0): 0.0
}

# Probabilidad conjunta usando regla de la cadena
joint_probs = {}
for L in [0,1]:
    for R in [0,1]:
        for C in [0,1]:
            joint_probs[(L,R,C)] = P_Lluvia**L * (1-P_Lluvia)**(1-L) * \
                                   P_Riego**R * (1-P_Riego)**(1-R) * \
                                   (P_Calle_given[(L,R)]**C * (1-P_Calle_given[(L,R)])**(1-C))

# Mostrar algunas probabilidades conjuntas
for key, val in joint_probs.items():
    print(f"P(Lluvia={key[0]}, Riego={key[1]}, Calle={key[2]}) = {val:.4f}")
