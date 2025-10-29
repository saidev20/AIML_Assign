import random                                       
import math
def fitness(ind):
    x, y = ind
    return x * math.sin(y) + y * math.cos(x)
def create_ind():
    return [random.uniform(0, 10), random.uniform(0, 10)]
def crossover(p1, p2):
    a = random.random()
    return [(a * p1[0] + (1-a) * p2[0]), (a * p1[1] + (1-a) * p2[1])]
def mutate(ind, rate=0.1):
    if random.random() < rate:
        ind[0] += random.uniform(-1, 1)
        ind[1] += random.uniform(-1, 1)
    ind[0] = max(0, min(10, ind[0]))
    ind[1] = max(0, min(10, ind[1]))
    return ind
POP_SIZE = 10
GENS = 20
population = [create_ind() for _ in range(POP_SIZE)]
print("Gen |    Best X    |    Best Y    | Fitness")
print("----------------------------------------------")
for gen in range(GENS):
    scored = [(ind, fitness(ind)) for ind in population]
    scored.sort(key=lambda x: x[1], reverse=True)
    best = scored[0][0]
    best_fit = scored[0][1]
    print(f"{gen:3d} | {best[0]:11.4f} | {best[1]:11.4f} | {best_fit:.4f}")
    parents = [s[0] for s in scored[:POP_SIZE // 2]]
    new_pop = []
    while len(new_pop) < POP_SIZE:
        p1, p2 = random.sample(parents, 2)
        child = crossover(p1, p2)
        child = mutate(child)
        new_pop.append(child)
    population = new_pop
best = max(population, key=fitness)
print("\nFinal Best:")
print(f"X = {best[0]:.4f}, Y = {best[1]:.4f}, Fitness = {fitness(best):.4f}")
