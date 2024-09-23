import numpy as np

def f(x):
    return x**3 - 6*x + 14

def binary_to_real(binary_vector):
    decimal = int(''.join(map(str, binary_vector)), 2)
    return -10 + (decimal / (2**len(binary_vector) - 1)) * 20

def initialize_population(pop_size, binary_length):
    return [np.random.randint(0, 2, binary_length).tolist() for _ in range(pop_size)]

def tournament_selection(population, fitness, tournament_size=2):
    selected = np.random.choice(range(len(population)), tournament_size, replace=False)
    return population[selected[np.argmin(fitness[selected])]]

def crossover(parent1, parent2, crossover_points):
    child1, child2 = parent1.copy(), parent2.copy()
    for point in crossover_points:
        if point < len(parent1):
            child1[point], child2[point] = parent2[point], parent1[point]
    return child1, child2

def mutate(individual, mutation_rate):
    for i in range(len(individual)):
        if np.random.rand() < mutation_rate:
            individual[i] = 1 - individual[i]

def apply_elitism(population, fitness, elitism_rate):
    elite_count = int(elitism_rate * len(population))
    elite_indices = np.argsort(fitness)[:elite_count]
    return [population[i] for i in elite_indices]

def genetic_algorithm(pop_size=10, mutation_rate=0.01, crossover_points_count=1, 
                elitism=False, elitism_rate=0.1, max_generations=1000, binary_length=20):

    population = initialize_population(pop_size, binary_length)
    best_solution = None
    best_fitness = float('inf')

    for generation in range(max_generations):
        fitness = np.array([f(binary_to_real(ind)) for ind in population])

        if np.min(fitness) < best_fitness:
            best_fitness = np.min(fitness)
            best_solution = population[np.argmin(fitness)]
        
        new_population = []

        # Aplicando elitismo
        if elitism:
            elite_individuals = apply_elitism(population, fitness, elitism_rate)
            new_population.extend(elite_individuals)

        while len(new_population) < pop_size:
            parent1 = tournament_selection(population, fitness)
            parent2 = tournament_selection(population, fitness)

            # Crossover
            crossover_points = np.random.choice(range(binary_length), crossover_points_count, replace=False)
            child1, child2 = crossover(parent1, parent2, crossover_points)

            # Mutação
            mutate(child1, mutation_rate)
            mutate(child2, mutation_rate)

            new_population.append(child1)
            if len(new_population) < pop_size:
                new_population.append(child2)

        population = new_population

    best_x = binary_to_real(best_solution)
    return best_x, f(best_x)

best_x, best_fitness = genetic_algorithm()
print(f"Melhor valor de x: {best_x}, com f(x): {best_fitness}")
