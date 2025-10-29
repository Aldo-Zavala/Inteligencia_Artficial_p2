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
for node, neighbors in graph.items():#iteramos por los nodos y sus vecinos
    for neighbor in neighbors:#iteramos por los vecinos
        G.add_edge(node, neighbor)#agregamos la arista al grafo

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

    return proccessed#retornamos los nodos procesados
result = bfs(graph, 'A')#llamamos a la funcion bfs con el grafo y el nodo inicial
print ("resultado : ",result) #imprimimos el resultado
plt.figure(figsize=(8, 6))#definimos el tamaño de la figura
pos = nx.spring_layout(G, seed=42)#definimos la posicion de los nodos
nx.draw(G, pos, with_labels=True, node_color='skyblue',#definimos el color de los nodos
        node_size=1500, font_size=12, font_weight='bold')#definimos el tamaño y el estilo de la fuente

plt.title("Grafo representado con NetworkX")
plt.show()                           #