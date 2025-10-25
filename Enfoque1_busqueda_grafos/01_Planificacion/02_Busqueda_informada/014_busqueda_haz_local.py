import heapq

def local_beam_search(graph, heuristic, start_nodes, k=2, max_iterations=10):
    beam = [(heuristic[n], n, [n]) for n in start_nodes]  # (valor, nodo, camino)
    
    for _ in range(max_iterations):
        successors = []
        
        # Expandir todos los nodos del haz actual
        for h_val, node, path in beam:
            for neighbor in graph[node]:
                new_path = path + [neighbor]
                successors.append((heuristic[neighbor], neighbor, new_path))
        
        if not successors:
            break
        
        # Seleccionar los k mejores sucesores
        beam = heapq.nlargest(k, successors, key=lambda x: x[0])
    
    # El mejor nodo encontrado
    best_value, best_node, best_path = max(beam, key=lambda x: x[0])
    return best_path, best_node, best_value

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

start_nodes = ['A', 'C']  # haz inicial
path, best_node, best_value = local_beam_search(graph, heuristic, start_nodes, k=2)
print("Camino recorrido:", path)
print("Mejor nodo encontrado:", best_node)
print("Valor heurístico:", best_value)