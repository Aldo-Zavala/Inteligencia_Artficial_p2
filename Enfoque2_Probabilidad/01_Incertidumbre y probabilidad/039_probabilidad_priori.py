# Probabilidades a priori y verosimilitudes
P_enfermo = 0.01       # prior
P_sano = 1 - P_enfermo

P_positivo_enfermo = 0.95  # verosimilitud
P_positivo_sano = 0.05

# Teorema de Bayes
P_enfermo_post = (P_positivo_enfermo * P_enfermo) / \
                 (P_positivo_enfermo * P_enfermo + P_positivo_sano * P_sano)

print(f"Probabilidad a posteriori de estar enfermo dado positivo: {P_enfermo_post:.2f}")
