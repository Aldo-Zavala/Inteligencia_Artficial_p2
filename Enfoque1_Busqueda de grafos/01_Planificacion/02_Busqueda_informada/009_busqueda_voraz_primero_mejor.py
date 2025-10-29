import heapq

def greedy_best_first_search(graph, start, goal, heuristic):
     # Cola de prioridad: (valor heurístico, nodo, camino recorrido)
    queue = []
    heapq.heappush(queue, (heuristic[start], start, [start]))
    visited = set()
    
    while queue:
        h, current, path = heapq.heappop(queue)
        
        if current == goal:
            return path
        
        if current not in visited:
            visited.add(current)
            
            for neighbor in graph[current]:
                if neighbor not in visited:#
                    heapq.heappush(queue, (heuristic[neighbor], neighbor, path + [neighbor]))
    
    return None  # si no se encuentra el objetivo

# Ejemplo de grafo
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Heurística (estimación de A->Goal F)
heuristic = {
    'A': 4,
    'B': 2,
    'C': 2,
    'D': 4,
    'E': 1,
    'F': 0
}

start = 'A'
goal = 'F'

path = greedy_best_first_search(graph, start, goal, heuristic)
print("Camino encontrado:", path)