def dfs_limitado(graph, start, goal, limit, depth=0, visited=None):
    if visited is None:
        visited = set()

    print(f"{'  '*depth} Visitando: {start} (profundidad {depth})")

    if start == goal:
        print(f"{'  '*depth} Encontrado {goal}")
        return [start]

    if depth >= limit:
        return None

    visited.add(start)

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            path = dfs_limitado(graph, neighbor, goal, limit, depth+1, visited)
            if path:
                return [start] + path

    return None


def profundidad_iterativa(graph, start, goal, max_depth):
    """
    Búsqueda en profundidad iterativa (IDDFS)
    """
    for limit in range(max_depth + 1):
        print(f"\n Intentando con límite de profundidad = {limit}")
        path = dfs_limitado(graph, start, goal, limit)
        if path:
            print(f"\n Nodo encontrado con profundidad {limit}")
            return path
    print("\nNo se encontró el objetivo dentro del límite de profundidad")
    return None


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

# Ejecutar el algoritmo
start_node = 'A'
goal_node = 'L'
max_depth = 5

path = profundidad_iterativa(graph, start_node, goal_node, max_depth)
print("\nRuta encontrada:", path)