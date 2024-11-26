#!/bin/python3

import numpy as np

observations = 1000

xs = np.random.uniform(-10, 10, size=(observations,1))
zs = np.random.uniform(-10, 10, size=(observations,1))

inputs = np.column_stack((xs, zs))

noise = np.random.uniform(-1, 1, (observations, 1))

targets = 2*xs + 3*zs + 5 + noise
init_range = 0.1

weights = np.random.uniform(-init_range, init_range, size=(2,1))
biases = np.random.uniform(-init_range, init_range, size=1)

learning_rate = 0.02

print(targets)