import random

# ----------------------
# GridWorld 4x3
# ----------------------
world = [
    [0, 0, 0, +1],
    [0, -1, 0, -1],
    [0, 0, 0, 0]
]

acciones = ['arriba','abajo','izquierda','derecha']

gamma = 0.9
episodios = 500
alpha = 0.1

# ----------------------
# Inicializar política aleatoria
# ----------------------
policy = {}
for i in range(3):
    for j in range(4):
        if world[i][j] != -1:
            policy[(i,j)] = random.choice(acciones)

# Inicializar valores de estado
V = {}
for i in range(3):
    for j in range(4):
        if world[i][j] != -1:
            V[(i,j)] = 0.0

# Función mover
def mover(pos, accion):
    i,j = pos
    if accion=='arriba':
        ni,nj = i-1,j
    elif accion=='abajo':
        ni,nj = i+1,j
    elif accion=='izquierda':
        ni,nj = i,j-1
    elif accion=='derecha':
        ni,nj = i,j+1
    else:
        ni,nj = i,j
    if 0<=ni<3 and 0<=nj<4 and world[ni][nj]!=-1:
        return (ni,nj)
    return pos

# ----------------------
# Búsqueda de política por iteración
# ----------------------
for _ in range(episodios):
    # Iterar sobre todos los estados
    for state in V:
        if world[state[0]][state[1]] in [1,-1]:
            continue
        # Evaluar cada acción
        mejores_val = -float('inf')
        mejor_accion = None
        for a in acciones:
            next_state = mover(state, a)
            recompensa = world[next_state[0]][next_state[1]]
            valor = recompensa + gamma * V[next_state]
            if valor > mejores_val:
                mejores_val = valor
                mejor_accion = a
        # Actualizar valor del estado
        V[state] = (1-alpha)*V[state] + alpha*mejores_val
        # Actualizar política
        policy[state] = mejor_accion

# ----------------------
# Mostrar política
# ----------------------
print("Política óptima encontrada:")
for i in range(3):
    fila = []
    for j in range(4):
        if (i,j) in policy:
            fila.append(policy[(i,j)][0].upper())
        else:
            fila.append(" # ")
    print(fila)
