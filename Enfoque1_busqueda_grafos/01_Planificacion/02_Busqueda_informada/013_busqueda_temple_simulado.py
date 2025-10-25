import math
import random

def simulated_annealing(graph, start, heuristic, max_iterations=50, initial_temp=10, cooling_rate=0.9):
    
    current = start
    best = start
    best_value = heuristic[start]
    temp = initial_temp
    path = [current]
    
    for i in range(max_iterations):
        neighbors = graph[current]
        if not neighbors:
            break
        
        # Elegir un vecino aleatorio
        next_node = random.choice(neighbors)
        delta = heuristic[next_node] - heuristic[current]
        
        # Si es mejor, aceptar; si es peor, aceptar con cierta probabilidad
        if delta > 0 or random.random() < math.exp(delta / temp):
            current = next_node
            path.append(current)
            
            if heuristic[current] > best_value:
                best = current
                best_value = heuristic[current]
        
        # Reducir temperatura
        temp *= cooling_rate
    
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
path, best_node, best_value = simulated_annealing(graph, start, heuristic)
print("Camino recorrido:", path)
print("Mejor nodo encontrado:", best_node)
print("Valor heurístico del mejor nodo:", best_value)