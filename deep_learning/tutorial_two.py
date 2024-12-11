#!/bin/python3

import numpy as np

# f(x) = y = 3 * x1 + 8 * x2 + 5

n = 8
feature = np.array([[1, 3], [2, 6], [3, 9], [4, 12], [5, 15], [6, 18], [7, 21], [8, 24]]) # 8*2
original_weight = np.array([[3], [8]])
target = np.dot(feature, original_weight) + 5
print(target)

etha = 0.002
weight = np.array([[1], [1]])
bias = np.array([[1]])

for i in range(50000):
    print(f"# Iteration {i+1}")
    output = np.dot(feature, weight) + bias
    loss = np.sum((output-target) ** 2)/2
    delta = output-target
    delta_scaled = delta/n
    weight = weight - etha * np.dot(feature.T, delta_scaled)
    bias = bias - etha * np.sum(delta_scaled)
    print(f"Current loss: {loss}")
    print(f"Updated weigth: {weight}")
    print(f"Updated bias: {bias}")
    print()