import random

# ----- ENTORNO -----
# Mapa del mundo (4x3)
# -1 = obstáculo, +1 = meta, -1 = trampa
world = [
    [0, 0, 0, +1],
    [0, -1, 0, -1],
    [0, 0, 0, 0]
]

# Política fija: siempre moverse a la derecha si se puede, sino hacia arriba
policy = {
    (0, 0): 'derecha', (0, 1): 'derecha', (0, 2): 'derecha',
    (1, 0): 'arriba', (1, 2): 'derecha',
    (2, 0): 'arriba', (2, 1): 'derecha', (2, 2): 'derecha'
}

# Posibles acciones
acciones = {
    'arriba': (-1, 0),
    'abajo': (1, 0),
    'izquierda': (0, -1),
    'derecha': (0, 1)
}

# ----- PARÁMETROS -----
alpha = 0.1      # tasa de aprendizaje
gamma = 0.9      # factor de descuento
episodios = 1000

# Valores iniciales
V = {}
for i in range(3):
    for j in range(4):
        if world[i][j] != -1:  # no se evalúa obstáculo
            V[(i, j)] = 0.0

# ----- FUNCIÓN AUXILIAR -----
def mover(pos, accion):
    i, j = pos
    di, dj = acciones[accion]
    ni, nj = i + di, j + dj
    if 0 <= ni < 3 and 0 <= nj < 4 and world[ni][nj] != -1:
        return (ni, nj)
    return pos  # si se sale o choca, se queda

# ----- APRENDIZAJE PASIVO -----
for _ in range(episodios):
    pos = (2, 0)  # estado inicial
    while True:
        if world[pos[0]][pos[1]] == +1 or world[pos[0]][pos[1]] == -1:
            break  # termina episodio

        accion = policy.get(pos, random.choice(list(acciones.keys())))
        nueva_pos = mover(pos, accion)

        recompensa = world[nueva_pos[0]][nueva_pos[1]]
        # Actualización TD (aprendizaje pasivo)
        V[pos] = V[pos] + alpha * (recompensa + gamma * V[nueva_pos] - V[pos])

        pos = nueva_pos

# ----- RESULTADOS -----
print("Valores aprendidos de los estados (V):\n")
for i in range(3):
    fila = []
    for j in range(4):
        if (i, j) in V:
            fila.append(f"{V[(i, j)]:6.2f}")
        else:
            fila.append("  ####")
    print(fila)
