import random

# -----------------------------
# Modelo del robot (DBN simple)
# -----------------------------

# Estados posibles
states = ["A", "B"]

# Transición entre tiempos: P(X_t | X_{t-1})
# Alta probabilidad de quedarse, pequeña de moverse
transition_model = {
    "A": {"A": 0.8, "B": 0.2},
    "B": {"A": 0.3, "B": 0.7},
}

# Sensor (lectura): P(E_t | X_t)
# Sensor es correcto el 90% del tiempo
sensor_model = {
    "A": {"A": 0.9, "B": 0.1},  # lectura "A" o "B"
    "B": {"A": 0.1, "B": 0.9},
}

# Belief inicial (distribución sobre estados)
belief = {"A": 0.5, "B": 0.5}


def normalize(d):
    total = sum(d.values())
    for k in d:
        d[k] /= total
    return d


def forward(belief_prev, evidence):
    """Actualiza la creencia al tiempo t dado el sensor E_t."""
    # Predicción: aplicar transición
    prediction = {}
    for s in states:
        prediction[s] = sum(belief_prev[s_prev] * transition_model[s_prev][s] for s_prev in states)

    # Actualización: incorporar observación (sensor)
    updated = {s: prediction[s] * sensor_model[s][evidence] for s in states}
    return normalize(updated)


# -----------------------------
# Simulación del proceso
# -----------------------------
true_state = random.choice(states)
print(f"Estado inicial real: {true_state}")
print(f"Belief inicial: {belief}\n")

for t in range(1, 6):
    # Avanza el estado real según el modelo
    r = random.random()
    if r < transition_model[true_state]["A"]:
        true_state = "A"
    else:
        true_state = "B"

    # Sensor genera observación
    obs = "A" if random.random() < sensor_model[true_state]["A"] else "B"

    # Actualiza creencia
    belief = forward(belief, obs)

    print(f"t={t}")
    print(f"  Estado real: {true_state}")
    print(f"  Observación (sensor): {obs}")
    print(f"  Nueva creencia: {belief}\n")
