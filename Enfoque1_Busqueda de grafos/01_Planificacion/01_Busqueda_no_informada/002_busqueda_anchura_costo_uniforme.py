import heapq
def uniform_cost_search(graph, start, goal):
    # Cola de prioridad: elementos (costo_acumulado, nodo, padre)
    frontier = []
    heapq.heappush(frontier, (0, start, None))
    # Para reconstruir ruta: mapa nodo -> (padre, costo_minimo_encontrado)
    came_from = {start: (None, 0)}

    # Mientras haya nodos por expandir
    while frontier:
        cost_so_far, node, parent = heapq.heappop(frontier)

        # Si extraemos un nodo con un coste mayor al mejor conocido, lo ignoramos
        if node in came_from and cost_so_far > came_from[node][1]:
            continue

        # Registrar el padre (ya guardado al insertar originalmente) — redundante aquí
        came_from[node] = (parent, cost_so_far)

        # Si llegamos al objetivo, reconstruimos la ruta
        if node == goal:
            path = []
            cur = goal
            total_cost = came_from[goal][1]
            while cur is not None:
                path.append(cur)
                cur = came_from[cur][0]
            path.reverse()
            return path, total_cost

        # Expandir vecinos
        for neighbor, weight in graph.get(node, []):
            new_cost = cost_so_far + weight
            # Si no conocemos al vecino o encontramos un coste mejor, lo añadimos a la frontera
            if (neighbor not in came_from) or (new_cost < came_from[neighbor][1]):
                came_from[neighbor] = (node, new_cost)
                heapq.heappush(frontier, (new_cost, neighbor, node))

    # Si la frontera se vacía y no alcanzamos goal
    return None, None
if __name__ == "__main__":
    # Grafo ponderado como diccionario: nodo -> [(vecino, peso), ...]
    graph = {
        'A': [('B', 2), ('C', 5), ('D', 1)],
        'B': [('E', 3), ('F', 1)],
        'C': [('F', 2)],
        'D': [('G', 2)],
        'E': [('H', 6)],
        'F': [('H', 2)],
        'G': [('H', 1)],
        'H': []
    }

    ruta, costo = uniform_cost_search(graph, 'A', 'H')
    if ruta is None:
        print("No existe ruta de A a H")
    else:
        print("Ruta de coste mínimo:", ruta)
        print("Costo total:", costo)#