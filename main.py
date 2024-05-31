import random

# Define the fitness function
def f(x, y):
    return x**2 + y**2

# Set the population size and number of iterations
POP_SIZE = 5
NUM_ITER = 20

# Initialize the population with random x and y values between -5 and 5
population = [[1, 2], [-2, 3], [4, -1], [5, 2], [-3, 3]]
#population = [[random.uniform(-5, 5), random.uniform(-5, 5)] for _ in range(POP_SIZE)]
print("Initial population:")
for i, individual in enumerate(population):
    print(f"{i+1}: {individual}")

# Run the evolutionary algorithm
for iter in range(NUM_ITER):
    offspring = []
    for i in range(POP_SIZE):
        # Binary tournament selection of parents
        p1 = random.choice(population)
        p2 = random.choice(population)
        parent1 = p1 if f(*p1) > f(*p2) else p2

        p1 = random.choice(population)
        p2 = random.choice(population)
        parent2 = p1 if f(*p1) > f(*p2) else p2

        # Generate 4 offspring per parent using crossover and mutation
        for j in range(4):
            # Crossover by taking x value of parent 1 and y value of parent 2
            child = [parent1[0], parent2[1]]

            # Mutation with a 50% mutation rate using swap mutation
            if random.random() < 0.5:
                child[0], child[1] = child[1], child[0]

            offspring.append(child)

    # Survivor selection using truncation
    population = sorted(offspring, key=lambda ind: -f(*ind))[:POP_SIZE]

    # Print the best individual of each generation
    bestIndividual = population[0]
    print(f"Best individual in iteration {iter+1}: x = {bestIndividual[0]}, y = {bestIndividual[1]}, fitness = {f(*bestIndividual)}")
