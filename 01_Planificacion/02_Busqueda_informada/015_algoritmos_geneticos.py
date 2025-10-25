import random

# Función de fitness (cuánto mejor es la solución)
def fitness(individuo):
    # Ejemplo: queremos maximizar la suma de genes
    return sum(individuo)

# Inicializar población
def inicializar_poblacion(tam_poblacion, tam_individuo):
    return [[random.randint(0,1) for _ in range(tam_individuo)] for _ in range(tam_poblacion)]

# Selección: torneo simple
def seleccion(poblacion, k=3):
    torneo = random.sample(poblacion, k)
    return max(torneo, key=fitness)

# Cruce: crossover de un punto
def crossover(padre1, padre2):
    punto = random.randint(1, len(padre1)-1)
    hijo1 = padre1[:punto] + padre2[punto:]
    hijo2 = padre2[:punto] + padre1[punto:]
    return hijo1, hijo2

# Mutación: cambiar un gen aleatoriamente
def mutacion(individuo, prob=0.1):
    return [1-g if random.random() < prob else g for g in individuo]

# Algoritmo Genético
def algoritmo_genetico(tam_poblacion=6, tam_individuo=5, generaciones=10):
    poblacion = inicializar_poblacion(tam_poblacion, tam_individuo)
    
    for gen in range(generaciones):
        nueva_poblacion = []
        while len(nueva_poblacion) < tam_poblacion:
            # Selección
            padre1 = seleccion(poblacion)
            padre2 = seleccion(poblacion)
            # Cruce
            hijo1, hijo2 = crossover(padre1, padre2)
            # Mutación
            hijo1 = mutacion(hijo1)
            hijo2 = mutacion(hijo2)
            nueva_poblacion.extend([hijo1, hijo2])
        poblacion = nueva_poblacion[:tam_poblacion]
        # Mejor de la generación
        mejor = max(poblacion, key=fitness)
        print(f"Generación {gen+1}: Mejor individuo {mejor}, Fitness={fitness(mejor)}")
    
    # Mejor de toda la ejecución
    mejor_global = max(poblacion, key=fitness)
    return mejor_global, fitness(mejor_global)

# Ejecutar
mejor_individuo, valor = algoritmo_genetico()
print("\nMejor solución final:", mejor_individuo, "Fitness:", valor)