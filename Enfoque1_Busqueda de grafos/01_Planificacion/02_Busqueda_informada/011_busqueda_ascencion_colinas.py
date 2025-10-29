def hill_climbing(graph, start, heuristic):
    current = start
    path = [current]
    
    while True:
        neighbors = graph[current]
        if not neighbors:
            break
        
        # Seleccionar vecino con mejor heurística
        next_node = max(neighbors, key=lambda n: heuristic[n])
        
        # Si el vecino no mejora, detenerse (óptimo local)
        if heuristic[next_node] <= heuristic[current]:
            break
        
        current = next_node
        path.append(current)
    
    return path, heuristic[current]

# Ejemplo de grafo
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Heurística (mayor = mejor)
heuristic = {
    'A': 1,
    'B': 3,
    'C': 2,
    'D': 5,
    'E': 4,
    'F': 6
}

start = 'A'
path, value = hill_climbing(graph, start, heuristic)
print("Camino encontrado:", path)
print("Valor heurístico final:", value)
