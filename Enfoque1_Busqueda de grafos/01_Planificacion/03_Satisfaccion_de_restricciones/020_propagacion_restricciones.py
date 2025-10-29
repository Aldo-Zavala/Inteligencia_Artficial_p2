# Variables y dominios
variables = ['A', 'B', 'C']
dominio = ['Rojo', 'Verde', 'Azul']

# Vecinos (restricciones)
vecinos = {
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B']
}

# Función para propagar restricciones
def propagar_restricciones(dominios):
    cambios = True
    while cambios:
        cambios = False
        for var in variables:
            if len(dominios[var]) == 1:  # si la variable tiene un valor fijo
                valor = dominios[var][0]
                for vecino in vecinos[var]:
                    if valor in dominios[vecino]:
                        dominios[vecino].remove(valor)
                        cambios = True
                        if not dominios[vecino]:
                            return False  # conflicto: dominio vacío
    return True

# Función CSP con backtracking y propagación de restricciones
def csp_propagacion(asignacion, dominios):
    if len(asignacion) == len(variables):
        return asignacion
    
    # Elegir variable no asignada
    var = next(v for v in variables if v not in asignacion)
    
    for valor in dominios[var]:
        asignacion[var] = valor
        dominios_copia = {v: list(dominios[v]) for v in dominios}
        dominios_copia[var] = [valor]
        
        if propagar_restricciones(dominios_copia):
            resultado = csp_propagacion(asignacion, dominios_copia)
            if resultado:
                return resultado
        
        del asignacion[var]
    
    return None

# Inicializar dominios
dominios_iniciales = {v: list(dominio) for v in variables}

# Ejecutar
solucion = csp_propagacion({}, dominios_iniciales)
print("Solución encontrada con propagación de restricciones:", solucion)
