# Evolutionary Algorithm README

## Overview

This script implements an evolutionary algorithm to optimize a simple fitness function \( f(x, y) = x^2 + y^2 \). The algorithm evolves a population of candidate solutions through selection, crossover, and mutation over multiple iterations.

## Prerequisites

Ensure you have Python installed. No additional packages are required for this script.

## Script Explanation

### Fitness Function

The fitness function \( f(x, y) \) calculates the fitness of an individual based on their \( x \) and \( y \) values:

```python
def f(x, y):
    return x**2 + y**2
```

### Parameters

- `POP_SIZE`: The number of individuals in the population.
- `NUM_ITER`: The number of iterations for the evolutionary algorithm.

### Initial Population

The initial population is defined with random \( x \) and \( y \) values between -5 and 5. You can use a predefined population or randomly initialize it:

```python
population = [[1, 2], [-2, 3], [4, -1], [5, 2], [-3, 3]]
# Or use the following for random initialization:
# population = [[random.uniform(-5, 5), random.uniform(-5, 5)] for _ in range(POP_SIZE)]
```

### Evolutionary Process

The script evolves the population over the specified number of iterations (`NUM_ITER`).

#### Selection

Parents are selected using binary tournament selection. Two parents are chosen based on their fitness:

```python
p1 = random.choice(population)
p2 = random.choice(population)
parent1 = p1 if f(*p1) > f(*p2) else p2

p1 = random.choice(population)
p2 = random.choice(population)
parent2 = p1 if f(*p1) > f(*p2) else p2
```

#### Crossover and Mutation

Four offspring are generated from each pair of parents using crossover and mutation:

- **Crossover**: The \( x \) value from parent 1 and the \( y \) value from parent 2 are combined.
- **Mutation**: With a 50% chance, the \( x \) and \( y \) values are swapped.

```python
child = [parent1[0], parent2[1]]
if random.random() < 0.5:
    child[0], child[1] = child[1], child[0]
offspring.append(child)
```

#### Survivor Selection

The population is updated by selecting the best individuals from the offspring based on their fitness:

```python
population = sorted(offspring, key=lambda ind: -f(*ind))[:POP_SIZE]
```

### Output

The script prints the best individual of each generation, showing their \( x \), \( y \) values, and fitness:

```python
print(f"Best individual in iteration {iter+1}: x = {bestIndividual[0]}, y = {bestIndividual[1]}, fitness = {f(*bestIndividual)}")
```

## Running the Script

1. Save the script to a Python file, e.g., `evolutionary_algorithm.py`.
2. Open a terminal or command prompt.
3. Navigate to the directory containing `evolutionary_algorithm.py`.
4. Run the script:

```sh
python evolutionary_algorithm.py
```

