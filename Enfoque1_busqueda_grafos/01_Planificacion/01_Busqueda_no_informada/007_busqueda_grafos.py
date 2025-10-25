from collections import deque

def busqueda_en_grafo(graph, start, goal=None, tipo="BFS"):
    visitados = set()
    cola = deque([start]) if tipo == "BFS" else [start]  # Cola o pila según tipo
    padres = {start: None}

    while cola:
        # Según el tipo, extraemos el siguiente nodo
        nodo_actual = cola.popleft() if tipo == "BFS" else cola.pop()

        print(f" Visitando: {nodo_actual}")

        # Si llegamos al objetivo
        if goal and nodo_actual == goal:
            print(f" Objetivo '{goal}' encontrado.")
            return reconstruir_camino(padres, start, goal)

        visitados.add(nodo_actual)

        # Recorremos los vecinos
        for vecino in graph.get(nodo_actual, []):
            if vecino not in visitados and vecino not in cola:
                padres[vecino] = nodo_actual
                if tipo == "BFS":
                    cola.append(vecino)
                else:
                    cola.append(vecino)

    print(" No se encontró el objetivo o ya se visitaron todos los nodos.")
    return list(visitados)


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


#  Ejemplo de grafo
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': [],
    'D': ['G','H'],
    'E': ['I','J'],
    'F': [],
    'G': ['K','L'],
    'H': [],
    'I': [],
    'J': [],
    'K': [],
    'L': []
}

# Ejecutar búsqueda
print("\n===  BÚSQUEDA EN ANCHURA (BFS) ===")
camino_bfs = busqueda_en_grafo(graph, 'A', 'L', tipo="BFS")
print("Camino encontrado:", camino_bfs)

print("\n===  BÚSQUEDA EN PROFUNDIDAD (DFS) ===")
camino_dfs = busqueda_en_grafo(graph, 'A', 'L', tipo="DFS")
print("Camino encontrado:", camino_dfs)