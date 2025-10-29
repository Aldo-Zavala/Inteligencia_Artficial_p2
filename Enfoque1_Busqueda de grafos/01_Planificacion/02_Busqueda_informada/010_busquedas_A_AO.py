import heapq

def a_star_search(graph, start, goal, cost, heuristic):
    queue = []
    heapq.heappush(queue, (heuristic[start], 0, start, [start]))  # (f, g, nodo, camino)
    visited = set()
    
    while queue:
        f, g, current, path = heapq.heappop(queue)
        
        if current == goal:
            return path, g
        
        if current not in visited:
            visited.add(current)
            for neighbor in graph[current]:
                if neighbor not in visited:
                    g_new = g + cost[(current, neighbor)]
                    f_new = g_new + heuristic[neighbor]
                    heapq.heappush(queue, (f_new, g_new, neighbor, path + [neighbor]))
                    
    return None, float('inf')

# Ejemplo de grafo
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

cost = {
    ('A','B'): 1,
    ('A','C'): 4,
    ('B','D'): 2,
    ('B','E'): 5,
    ('C','F'): 3,
    ('E','F'): 1
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 1,
    'E': 1,
    'F': 0
}

path, total_cost = a_star_search(graph, 'A', 'F', cost, heuristic)
print("Camino A*:", path)
print("Costo total:", total_cost)