def dfs_recursive(graph, start, visited=None, order=None):
    if visited is None:
        visited = set()
    if order is None:
        order = [] 
        visited.add(start)
    order.append(start)

    for neigh in graph.get(start, []):
        if neigh not in visited:
            dfs_recursive(graph, neigh, visited, order)

    return order

# Ejemplo
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': [],
    'D': ['G','H'],
    'E': ['I','J'],
    'F': [],
    'G': ['K','L'],
    'H': [], 'I': [], 'J': [], 'K': [], 'L': []
}
print("DFS recursiva:", dfs_recursive(graph, 'A'))