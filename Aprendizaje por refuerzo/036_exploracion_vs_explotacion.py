import random

# ----------------------
# GridWorld 4x3
# ----------------------
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
alpha = 0.5
gamma = 0.9
epsilon = 0.2   # Probabilidad de explorar
episodios = 10

# Inicializar Q
Q = {}
for i in range(3):
    for j in range(4):
        if world[i][j] != -1:
            for a in acciones:
                Q[((i,j),a)] = 0.0

def mover(pos, accion):
    i,j = pos
    di,dj = acciones[accion]
    ni,nj = i+di,j+dj
    if 0<=ni<3 and 0<=nj<4 and world[ni][nj]!=-1:
        return (ni,nj)
    return pos

# ----------------------
# Simulación: exploración vs explotación
# ----------------------
for ep in range(episodios):
    pos = (2,0)
    print(f"\nEpisodio {ep+1}")
    while world[pos[0]][pos[1]] not in [1,-1]:
        # Decidir acción: epsilon-greedy
        if random.random() < epsilon:
            accion = random.choice(list(acciones.keys()))
            modo = "Exploración"
        else:
            max_val = max(Q[(pos,a)] for a in acciones)
            mejores = [a for a in acciones if Q[(pos,a)]==max_val]
            accion = random.choice(mejores)
            modo = "Explotación"

        nueva_pos = mover(pos, accion)
        recompensa = world[nueva_pos[0]][nueva_pos[1]]

        # Actualización Q
        max_q_next = max(Q[(nueva_pos,a)] for a in acciones)
        Q[(pos,accion)] += alpha * (recompensa + gamma*max_q_next - Q[(pos,accion)])

        print(f"Estado: {pos}, Acción: {accion}, Modo: {modo}, Recompensa: {recompensa}")

        pos = nueva_pos
