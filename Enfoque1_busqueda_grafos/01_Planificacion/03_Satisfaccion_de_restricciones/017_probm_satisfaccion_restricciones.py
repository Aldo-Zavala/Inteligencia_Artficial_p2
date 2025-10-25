from itertools import product

# Variables y dominios
variables = ['A', 'B', 'C']
dominio = ['Rojo', 'Verde', 'Azul']

# Restricciones: vecinos no pueden tener el mismo color
vecinos = {
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B']
}

# Función que verifica si una asignación cumple las restricciones
def es_valida(asignacion):
    for var in vecinos:
        for vecino in vecinos[var]:
            if var in asignacion and vecino in asignacion:
                if asignacion[var] == asignacion[vecino]:
                    return False
    return True

# Algoritmo CSP por fuerza bruta (simple)
def csp_solver(variables, dominio):
    for valores in product(dominio, repeat=len(variables)):
        asignacion = dict(zip(variables, valores))
        if es_valida(asignacion):
            return asignacion
    return None

# Ejecutar
solucion = csp_solver(variables, dominio)
print("Solución encontrada:", solucion)
