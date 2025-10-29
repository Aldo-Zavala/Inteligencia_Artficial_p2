def online_search(graph, start, goal):
    current = start
    path = [current]
    visited = set()

    while current != goal:
        visited.add(current)
        neighbors = [n for n in graph[current] if n not in visited]
        
        if not neighbors:  # sin vecinos sin visitar, retroceder
            if len(path) > 1:
                path.pop()  # retroceder
                current = path[-1]
            else:
                return None  # sin solución
        else:
            # Elegir un vecino aleatorio (estrategia simple online)
            current = neighbors[0]#
            path.append(current)
    
    return path

# Ejemplo de grafo
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

start = 'A'
goal = 'F'
path = online_search(graph, start, goal)
print("Camino encontrado (online):", path)
