import random

# ----------------------
# ENTORNO: GridWorld 4x3
# ----------------------
# -1 = obstáculo, +1 = meta, -1 = trampa
world = [
    [0, 0, 0, +1],
    [0, -1, 0, -1],
    [0, 0, 0, 0]
]

acciones = {
    'arriba': (-1,0),
    'abajo': (1,0),
    'izquierda': (0,-1),
    'derecha': (0,1)
}

# Parámetros
alpha = 0.5     # tasa de aprendizaje
gamma = 0.9     # factor de descuento
epsilon = 0.1   # probabilidad de exploración
episodios = 2000

# Inicializar Q(s,a) = 0
Q = {}
for i in range(3):
    for j in range(4):
        if world[i][j] != -1:
            for a in acciones:
                Q[((i,j),a)] = 0.0

# Función mover
def mover(pos, accion):
    i,j = pos
    di,dj = acciones[accion]
    ni,nj = i+di,j+dj
    if 0<=ni<3 and 0<=nj<4 and world[ni][nj] != -1:
        return (ni,nj)
    return pos

# ----------------------
# Q-Learning
# ----------------------
for _ in range(episodios):
    pos = (2,0)  # estado inicial
    while world[pos[0]][pos[1]] not in [1,-1]:
        # epsilon-greedy
        if random.random() < epsilon:
            accion = random.choice(list(acciones.keys()))
        else:
            max_val = max(Q[(pos,a)] for a in acciones)
            mejor_acciones = [a for a in acciones if Q[(pos,a)]==max_val]
            accion = random.choice(mejor_acciones)

        nueva_pos = mover(pos,accion)
        recompensa = world[nueva_pos[0]][nueva_pos[1]]

        # Actualización Q
        max_q_next = max(Q[(nueva_pos,a)] for a in acciones)
        Q[(pos,accion)] += alpha * (recompensa + gamma*max_q_next - Q[(pos,accion)])

        pos = nueva_pos

# ----------------------
# Extraer política óptima
# ----------------------
policy = {}
for i in range(3):
    for j in range(4):
        if world[i][j] != -1:
            q_vals = {a: Q[((i,j),a)] for a in acciones}
            policy[(i,j)] = max(q_vals, key=q_vals.get)

# Mostrar política
print("Política óptima aprendida:")
for i in range(3):
    fila = []
    for j in range(4):
        if (i,j) in policy:
            fila.append(policy[(i,j)][0].upper())
        else:
            fila.append(" # ")
    print(fila)
