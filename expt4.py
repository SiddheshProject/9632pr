import random
import numpy as np

def create_random_route(num_cities):
    route = list(range(num_cities))
    random.shuffle(route)
    return route

def calculate_total_distance(route, distances):
    total_distance = 0
    for i in range(len(route)):
        total_distance += distances[route[i-1]][route[i]]
    return total_distance

def crossover(parent1, parent2):
    # Order Crossover (OX)
    start, end = sorted(random.sample(range(len(parent1)), 2))
    offspring = [-1] * len(parent1)
    for i in range(start, end + 1):
        offspring[i] = parent1[i]
    for i in range(len(parent2)):
        if parent2[i] not in offspring:
            for j in range(len(offspring)):
                if offspring[j] == -1:
                    offspring[j] = parent2[i]
                    break
    return offspring

def mutate(route):
    # Swap Mutation
    idx1, idx2 = random.sample(range(len(route)), 2)
    route[idx1], route[idx2] = route[idx2], route[idx1]
    return route

def get_distances_from_input():
    num_cities = int(input("Enter the number of cities: "))
    distances = []
    print("Enter the distances between the cities (separated by spaces):")
    for _ in range(num_cities):
        distances.append(list(map(int, input().split())))
    return np.array(distances)

def genetic_algorithm(distances, population_size=100, num_generations=1000):
    num_cities = len(distances)
    population = [create_random_route(num_cities) for _ in range(population_size)]

    for _ in range(num_generations):
        new_population = []

        # Elitism: Keep the best route from the previous generation
        best_route = min(population, key=lambda x: calculate_total_distance(x, distances))
        new_population.append(best_route)

        while len(new_population) < population_size:
            parent1, parent2 = random.choices(population, k=2)
            offspring = crossover(parent1, parent2)
            if random.random() < 0.1:
                offspring = mutate(offspring)
            new_population.append(offspring)

        population = new_population

    best_route = min(population, key=lambda x: calculate_total_distance(x, distances))
    best_distance = calculate_total_distance(best_route, distances)
    return best_route, best_distance

if __name__ == "__main__":
    distances = get_distances_from_input()
    best_route, best_distance = genetic_algorithm(distances)
    print(f"Best route: {best_route}")
    print(f"Best distance: {best_distance}")
