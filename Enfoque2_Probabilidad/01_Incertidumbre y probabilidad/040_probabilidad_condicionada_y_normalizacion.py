# Priors
priors = {"H1": 0.5, "H2": 0.3, "H3": 0.2}
# Verosimilitud P(E|Hi)
likelihood = {"H1": 0.7, "H2": 0.2, "H3": 0.1}

# Probabilidades no normalizadas
unnormalized = {h: priors[h]*likelihood[h] for h in priors}

# Normalización
Z = sum(unnormalized.values())
posterior = {h: unnormalized[h]/Z for h in unnormalized}

print("Probabilidades a posteriori normalizadas:")
for h, p in posterior.items():
    print(f"{h}: {p:.3f}")
