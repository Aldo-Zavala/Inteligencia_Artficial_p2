def dfs_limitado(graph, start, goal, limit, depth=0, visited=None):
    if visited is None:
        visited = set()

    print(f"{'  '*depth} Visitando: {start} (profundidad {depth})")

    # Caso base: si encontramos el objetivo
    if start == goal:
        print(f"{'  '*depth} Encontrado {goal}")
        return [start]

    # Si llegamos al límite de profundidad
    if depth >= limit:
        print(f"{'  '*depth}Límite alcanzado en {start}")
        return None

    visited.add(start)

    # Exploramos los vecinos
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            path = dfs_limitado(graph, neighbor, goal, limit, depth+1, visited)
            if path:
                return [start] + path

    return None
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': [],
    'D': ['G', 'H'],
    'E': ['I', 'J'],
    'F': [],
    'G': ['K', 'L'],
    'H': [],
    'I': [],
    'J': [],
    'K': [],
    'L': []
}

#  Ejecutar la búsqueda
start_node = 'A'
goal_node = 'L'
limit = 3  # profundidad máxima

path = dfs_limitado(graph, start_node, goal_node, limit)
print("\nRuta encontrada:", path)