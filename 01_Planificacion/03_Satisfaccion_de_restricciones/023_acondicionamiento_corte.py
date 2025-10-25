from itertools import product

# Variables y dominios
variables = ['A', 'B', 'C', 'D']
dominio = ['Rojo', 'Verde', 'Azul']

# Vecinos (restricciones)
vecinos = {
    'A': ['B', 'D'],
    'B': ['A', 'C'],
    'C': ['B', 'D'],
    'D': ['A', 'C']
}

# Función para verificar consistencia parcial
def es_valida(asignacion, var, valor):
    for vecino in vecinos[var]:
        if vecino in asignacion and asignacion[vecino] == valor:
            return False
    return True

# Cutset Conditioning
def cutset_conditioning(cutset, resto_variables):
    # Probar todas las asignaciones posibles del cutset
    for valores_cutset in product(dominio, repeat=len(cutset)):
        asignacion = dict(zip(cutset, valores_cutset))
        
        # Resolver resto del CSP acíclico por backtracking simple
        if resolver_restante(asignacion, resto_variables):
            return asignacion
    return None

# Resolver resto de variables acíclicas
def resolver_restante(asignacion, variables_restantes):
    if not variables_restantes:
        return True  # todas asignadas
    
    var = variables_restantes[0]
    for valor in dominio:
        if es_valida(asignacion, var, valor):
            asignacion[var] = valor
            if resolver_restante(asignacion, variables_restantes[1:]):
                return True
            del asignacion[var]
    return False

# Identificar cutset (por ejemplo, A y C rompen el ciclo)
cutset = ['A', 'C']
resto = [v for v in variables if v not in cutset]

# Ejecutar Cutset Conditioning
solucion = cutset_conditioning(cutset, resto)
print("Solución encontrada con Cutset Conditioning:", solucion)