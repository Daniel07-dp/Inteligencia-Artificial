import random

#Función de aptitud que mide la distancia entre los puntos
def fitness(chromosome):
    distance = max(chromosome) - min(chromosome)
    return distance

#Función de cruce
def crossover(chromosome1, chromosome2):
    crossover_point = random.randint(1,2)
    offspring1 = chromosome1[:crossover_point] + chromosome2[crossover_point:]
    offspring2 = chromosome2[:crossover_point] + chromosome1[crossover_point:]
    return offspring1, offspring2

#Función de mutación
def mutation(chromosome):
    mutation_point = random.randint(0,2)
    chromosome[mutation_point] = random.uniform(0, 10)
    return chromosome

#Inicialización de la población
population = [[random.uniform(0,10) for _ in range(3)] for _ in range(10)]

#Parámetros del algoritmo
num_generations = 100
mutation_rate = 0.1