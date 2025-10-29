# Variables y dominios
variables = ['A', 'B', 'C']
dominio = ['Rojo', 'Verde', 'Azul']

# Vecinos (restricciones)
vecinos = {
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B']
}

# Función que hace backtracking con forward checking
def forward_checking(asignacion, dominios):
    if len(asignacion) == len(variables):
        return asignacion  # solución completa
    
    # Elegir siguiente variable no asignada
    var = next(v for v in variables if v not in asignacion)
    
    for valor in dominios[var]:
        # Crear copia de dominios para probar
        dominios_copia = {v: list(dominios[v]) for v in dominios}
        asignacion[var] = valor
        
        # Comprobación hacia adelante: eliminar valor de los vecinos
        conflict = False
        for vecino in vecinos[var]:
            if vecino not in asignacion and valor in dominios_copia[vecino]:
                dominios_copia[vecino].remove(valor)
                if not dominios_copia[vecino]:  # sin valores posibles -> conflicto
                    conflict = True
                    break
        
        if not conflict:
            resultado = forward_checking(asignacion, dominios_copia)
            if resultado:
                return resultado
        
        # Si falla, retroceder
        del asignacion[var]
    
    return None

# Inicializar dominios
dominios_iniciales = {v: list(dominio) for v in variables}

# Ejecutar
solucion = forward_checking({}, dominios_iniciales)
print("Solución encontrada con forward checking:", solucion)
