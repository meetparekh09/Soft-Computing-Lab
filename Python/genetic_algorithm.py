"""Solves Travelling Salesman Problem by using Genetic Algorithm."""

import numpy as np
from scipy.spatial.distance import euclidean
from numpy.random import randint, shuffle
from pprint import pprint as pp
import random


num_cities = 10
crossover_rate = 0.8
mutation_rate = 0.2
tolerance = 0.001
cities = np.array([(randint(low = 0, high = 10), randint(low = 0, high = 10)) for _ in range(num_cities)])


class Chromosome:
    """Stores the population and corresponding fitness"""

    def __init__(self, population, path = []):
        if len(path) == 0:
            self.path = population.copy()
            self.fitness = self._fitness(self.path)
        else:
            self.path = path
            self.fitness = self._fitness(self.path)


    def _fitness(self, chromosome):
        global cities
        dist = 0
        for i in range(len(chromosome)):
            dist += euclidean(cities[chromosome[i]], cities[chromosome[(i + 1) % len(chromosome)]])
        return 10/dist


    def crossover(self, chromosome):
        path = self.path.copy()
        break_point = randint(0, 10)
        for ind, num in enumerate(chromosome.path[break_point:]):
            path[break_point+ind], path[path.index(num)] = path[path.index(num)], path[break_point+ind]
        nChromosome = Chromosome(population = [], path = path)
        return nChromosome

    def mutation(self):
        a, b = randint(0, 10), randint(0, 10)
        self.path[a], self.path[b] = self.path[b], self.path[a]
        self.fitness = self._fitness(self.path)


def selection(chromosomes):
    max = np.sum(chromosome.fitness for chromosome in chromosomes)
    pick = random.uniform(0, max)
    current = 0
    for chromosome in chromosomes:
        current += chromosome.fitness
        if current > pick:
            return chromosome



def seed(population, samples = 100):
    generation = set()
    chromosomes = []
    count = 0
    while count <= samples:
        chromosome = population.copy()
        shuffle(chromosome)
        if tuple(chromosome) not in generation:
            generation.add(tuple(chromosome))
            chromosomes.append(Chromosome(chromosome))
            count += 1
    return chromosomes


def main():
    global crossover_rate, mutation_rate, num_cities
    pop = list(range(num_cities))
    chromosomes = seed(pop)
    iterations = 1000
    best_fitness = max([chromosome.fitness for chromosome in chromosomes])
    best_solution = chromosomes[np.argmax([chromosome.fitness for chromosome in chromosomes])]
    for i in range(iterations):
        num = random.random()
        if num > 1 - crossover_rate:
            parent1 = selection(chromosomes)
            parent2 = selection(chromosomes)
            while parent2 == parent1:
                parent2 = selection(chromosomes)
            child1 = parent1.crossover(parent1)
            child2 = parent1.crossover(parent2)
            if num > 1 - mutation_rate:
                child1.mutation()
            chromosomes[chromosomes.index(parent1)] = child1
            chromosomes[chromosomes.index(parent2)] = child2
        best_fitness1 = max([chromosome.fitness for chromosome in chromosomes])
        best_solution1 = chromosomes[np.argmax([chromosome.fitness for chromosome in chromosomes])]
        if best_fitness1 - best_fitness > tolerance:
            best_fitness = best_fitness1
            best_solution = best_solution1
        if (i + 1)%100 == 0:
            print("After {} Iterations, Best Fitness Uptil Now :: {}".format(i+1, best_fitness))
            print("Best Solution uptil {} Iterations :: {}".format(i+1, best_solution.path))


if __name__ == '__main__':
    main()
