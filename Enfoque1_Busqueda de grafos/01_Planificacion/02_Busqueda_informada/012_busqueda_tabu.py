import random

def tabu_search(graph, start, heuristic, max_iterations=20, tabu_size=5):
    current = start
    best = start
    best_value = heuristic[start]
    
    tabu_list = [current]
    path = [current]
    
    for _ in range(max_iterations):
        neighbors = [n for n in graph[current] if n not in tabu_list]
        if not neighbors:
            break#
        
        # Seleccionar vecino con mejor heurística
        next_node = max(neighbors, key=lambda n: heuristic[n])
        current = next_node
        path.append(current)
        
        # Actualizar lista tabú
        tabu_list.append(current)
        if len(tabu_list) > tabu_size:
            tabu_list.pop(0)
        
        # Actualizar mejor solución encontrada
        if heuristic[current] > best_value:
            best = current
            best_value = heuristic[current]
    
    return path, best, best_value

# Ejemplo de grafo
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

heuristic = {
    'A': 1,
    'B': 3,
    'C': 2,
    'D': 5,
    'E': 4,
    'F': 6
}

start = 'A'
path, best_node, best_value = tabu_search(graph, start, heuristic)
print("Camino recorrido:", path)
print("Mejor nodo encontrado:", best_node)
print("Valor heurístico del mejor nodo:", best_value)
