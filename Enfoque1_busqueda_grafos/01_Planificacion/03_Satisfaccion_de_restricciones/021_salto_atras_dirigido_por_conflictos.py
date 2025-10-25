# Variables y dominios
variables = ['A', 'B', 'C']
dominio = ['Rojo', 'Verde', 'Azul']

# Vecinos (restricciones)
vecinos = {
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B']
}

# Verifica si la asignación parcial es válida
def es_valida(var, valor, asignacion):
    for vecino in vecinos[var]:
        if vecino in asignacion and asignacion[vecino] == valor:
            return False
    return True

# Conflict-Directed Backjumping
def cbj(asignacion, index=0, conflictos=None):
    if conflictos is None:
        conflictos = {v: set() for v in variables}
    
    if index == len(variables):
        return asignacion  # solución completa
    
    var = variables[index]
    
    for valor in dominio:
        if es_valida(var, valor, asignacion):
            asignacion[var] = valor
            resultado = cbj(asignacion, index + 1, conflictos)
            if resultado:
                return resultado
            del asignacion[var]
        else:
            # Registrar conflicto con vecinos
            for vecino in vecinos[var]:
                if vecino in asignacion:
                    conflictos[var].add(vecino)
    
    # Determinar variable a retroceder
    if conflictos[var]:
        salto_a = max(conflictos[var], key=lambda v: variables.index(v))
        if variables.index(salto_a) < index:
            return None  # retrocede al nodo conflictivo
    return None

# Ejecutar
solucion = cbj({})
print("Solución encontrada con Conflict-Directed Backjumping:", solucion)
