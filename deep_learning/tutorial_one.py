#!/bin/python3

import numpy as np

observations = 1000

xs = np.random.uniform(-10, 10, size=(observations,1))
zs = np.random.uniform(-10, 10, size=(observations,1))

inputs = np.column_stack((xs, zs))

noise = np.random.uniform(-1, 1, (observations, 1))

targets = 2*xs + 3*zs + 5 + noise
init_range = 0.1


# Initial values
weights = np.random.uniform(-init_range, init_range, size=(2,1))
biases = np.random.uniform(-init_range, init_range, size=1)
learning_rate = 0.02

for _ in range(100):
    outputs = np.dot(inputs, weights) + biases
    deltas = outputs - targets
    loss = np.sum(deltas ** 2) / 2 / observations
    print(loss)
    deltas_scaled = deltas/observations
    weights = weights - learning_rate*np.dot(inputs.T, deltas_scaled)
    biases = biases - learning_rate*np.sum(deltas_scaled)

print(weights)
print(biases)