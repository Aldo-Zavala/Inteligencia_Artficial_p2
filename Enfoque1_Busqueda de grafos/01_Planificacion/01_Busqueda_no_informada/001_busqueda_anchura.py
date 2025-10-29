from collections import deque
import matplotlib.pyplot as plt
import networkx as nx

graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': [],
    'D': ['G','H' ],
    'E': ['I','J'],
    'F': [],
    'G': ['K', 'L'],
    'H': [],
    'I': [],
    'J': [],
    'K': [],   
    'L': []
}
G = nx.Graph()
for node, neighbors in graph.items():
    for neighbor in neighbors:
        G.add_edge(node, neighbor)

def bfs(graph, start_node):
    queue = deque([start_node])#inicializamos la cola con el nodo inicial
    proccessed = []
    
    while queue:#mientras la cola
        current_node = queue.popleft()
        #pop left nos va a retornar el primer elemento de la cola

        if current_node not in proccessed:#si el nodo no es parte de los procesados
            proccessed.append(current_node)#lo agegamos a los procesados

            for neighbor in graph[current_node]:#iteramos por los vecinos del nodo actual         
                if neighbor not in proccessed:#si el vecino no es parte de los procesados
                    queue.append(neighbor)#lo agregamos a la cola

    return proccessed
result = bfs(graph, 'A')
print ("resultado : ",result) 
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_color='skyblue',
        node_size=1500, font_size=12, font_weight='bold')

plt.title("Grafo representado con NetworkX")
plt.show()                           