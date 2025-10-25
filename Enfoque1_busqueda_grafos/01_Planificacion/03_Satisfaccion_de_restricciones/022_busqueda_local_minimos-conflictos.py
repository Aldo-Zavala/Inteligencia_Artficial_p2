import random

# Variables y dominios
variables = ['A', 'B', 'C']
dominio = ['Rojo', 'Verde', 'Azul']

# Vecinos (restricciones)
vecinos = {
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B']
}

# Contar conflictos de una variable
def contar_conflictos(var, valor, asignacion):
    return sum(1 for vecino in vecinos[var] if vecino in asignacion and asignacion[vecino] == valor)

# Algoritmo Min-Conflicts
def min_conflicts(max_iter=100):
    # Inicializar asignación aleatoria
    asignacion = {v: random.choice(dominio) for v in variables}
    
    for i in range(max_iter):
        # Lista de variables en conflicto
        conflicted = [v for v in variables if contar_conflictos(v, asignacion[v], asignacion) > 0]
        if not conflicted:
            return asignacion  # solución encontrada
        
        # Elegir una variable en conflicto aleatoria
        var = random.choice(conflicted)
        
        # Asignarle el valor que minimiza conflictos
        valor_min = min(dominio, key=lambda val: contar_conflictos(var, val, asignacion))
        asignacion[var] = valor_min
    
    return None  # si no se encuentra solución en max_iter

# Ejecutar
solucion = min_conflicts()
print("Solución encontrada con Min-Conflicts:", solucion)