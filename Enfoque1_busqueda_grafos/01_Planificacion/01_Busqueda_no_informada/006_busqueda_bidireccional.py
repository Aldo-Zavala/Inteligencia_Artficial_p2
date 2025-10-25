from collections import deque

def bidirectional_search(graph, start, goal):
    if start == goal:
        return [start]

    # Colas de búsqueda (una desde inicio y otra desde meta)
    forward_queue = deque([start])
    backward_queue = deque([goal])

    # Visitados desde ambos lados
    forward_visited = {start: None}  # nodo: padre
    backward_visited = {goal: None}

    while forward_queue and backward_queue:
        # --- Expansión desde el inicio ---
        current_forward = forward_queue.popleft()
        print(f" Expandiendo (inicio): {current_forward}")
        for neighbor in graph.get(current_forward, []):
            if neighbor not in forward_visited:
                forward_visited[neighbor] = current_forward
                forward_queue.append(neighbor)
                if neighbor in backward_visited:
                    # Se encontraron las dos búsquedas
                    return build_path(forward_visited, backward_visited, neighbor)

        # --- Expansión desde la meta ---
        current_backward = backward_queue.popleft()
        print(f" Expandiendo (meta): {current_backward}")
        for neighbor in graph.get(current_backward, []):
            if neighbor not in backward_visited:
                backward_visited[neighbor] = current_backward
                backward_queue.append(neighbor)
                if neighbor in forward_visited:
                    # Se encontraron las dos búsquedas
                    return build_path(forward_visited, backward_visited, neighbor)

    return None


def build_path(forward_visited, backward_visited, meeting_node):
    """Reconstruye la ruta completa al encontrarse las dos búsquedas"""
    # Desde inicio hasta el punto de encuentro
    path_forward = []
    node = meeting_node
    while node is not None:
        path_forward.append(node)
        node = forward_visited[node]
    path_forward.reverse()

    # Desde el punto de encuentro hasta el objetivo
    path_backward = []
    node = backward_visited[meeting_node]
    while node is not None:
        path_backward.append(node)
        node = backward_visited[node]

    return path_forward + path_backward


#  Ejemplo de grafo
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'G'],
    'F': ['C', 'H'],
    'G': ['E', 'H'],
    'H': ['F', 'G']
}

#  Ejecutar la búsqueda
start_node = 'A'
goal_node = 'H'
path = bidirectional_search(graph, start_node, goal_node)

print("\n Ruta encontrada:", path)