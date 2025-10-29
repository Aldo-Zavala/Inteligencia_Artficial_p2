import heapq

def greedy_best_first_search(graph, start, goal, heuristica):
    frontera = []
    heapq.heappush(frontera, (heuristica[start], start))  # (h(n), nodo)
    visitados = set()
    padres = {start: None}

    while frontera:
        _, actual = heapq.heappop(frontera)
        print(f" Visitando: {actual}")

        if actual == goal:
            print(" Objetivo encontrado.")
            return reconstruir_camino(padres, start, goal)

        visitados.add(actual)

        for vecino, costo in graph.get(actual, []):
            if vecino not in visitados:
                padres[vecino] = actual
                heapq.heappush(frontera, (heuristica[vecino], vecino))

    print(" No se encontró una ruta al objetivo.")
    return None


def reconstruir_camino(padres, inicio, objetivo):
    """Reconstruye el camino desde inicio hasta objetivo"""
    camino = [objetivo]
    while camino[-1] != inicio:
        padre = padres[camino[-1]]
        if padre is None:
            break
        camino.append(padre)
    camino.reverse()
    return camino


#  Grafo de ejemplo (con costos, pero no se usan directamente en Greedy)
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [('G', 2)],
    'E': [('G', 5)],
    'F': [('G', 2)],
    'G': []
}

#  Heurística (distancia estimada al objetivo 'G')
heuristica = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 2,
    'E': 5,
    'F': 3,
    'G': 0
}

#  Ejecutar búsqueda
start_node = 'A'
goal_node = 'G'
camino = greedy_best_first_search(graph, start_node, goal_node, heuristica)

print("\n Camino encontrado:", camino)#