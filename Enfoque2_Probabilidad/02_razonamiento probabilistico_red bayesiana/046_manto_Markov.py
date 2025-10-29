import random

# Estados: 0,1,2
estados = [0,1,2]

# Acciones: izquierda (-1), derecha (+1)
acciones = [-1, 1]

# Función de transición estocástica: depende solo del estado actual
def siguiente_estado(s, a):
    # 80% éxito, 20% quedarse
    if random.random() < 0.8:
        s_new = s + a
        if s_new < 0: s_new = 0
        if s_new > 2: s_new = 2
        return s_new
    else:
        return s  # falla, permanece en el mismo estado

# Simulación
s = 1  # estado inicial
for t in range(5):
    a = random.choice(acciones)
    s = siguiente_estado(s, a)
    print(f"Paso {t+1}: Estado actual = {s}, Acción tomada = {a}")
