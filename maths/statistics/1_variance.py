#!/bin/python3

import math
import matplotlib.pyplot as plt
import statistics
from colorama import Fore, Style
'''

Variance measures the dispersion of a set of data points around their mean
i.e measure of data dispersion
i.e variability around mean
i.e measure of variability

denoted by sigma^2 for population and S^2 for sample
'''

apple_price_usa = list(range(1, 11))
print(f"Prices of apple from 10 different shops in USA: {apple_price_usa}")
n = len(apple_price_usa)

# denoted by mew for popluation and x bar for sample
mean = sum(apple_price_usa)/n
print(f"Mean: {mean}")

# for population
population_variance = sum([math.pow(n - mean, 2) for n in apple_price_usa])/n
print(f"Population variance: {population_variance}")

# for sample
sample_variance = sum([math.pow(n - mean, 2) for n in apple_price_usa])/(n-1)
print(f"sample variance: {sample_variance}")

'''
Standard deviation: root(variance)
denoted by sigma for population and S for sample
'''

# Formula same for both population and sample
population_std = math.sqrt(population_variance)
print(f"Population std: {population_std}")
sample_std = math.sqrt(sample_variance)
print(f"Sample std: {sample_std}")

'''
Coefficient of variation (cv)
aka Relative Standard Deviation 

used to compare variability of different dataset. Comparing variability (stand deviation) of different dataset is meaningless therefore we have to use cv to compare variablity
'''

# Formula same for both population and sample
population_cv = population_std/mean
print(f"Population cv: {population_cv}")
sample_cv = sample_std/mean
print(f"Sample cv: {sample_cv}")

apple_price_india = [n*9 for n in range(1, 11)]
print(f"Prices of apple from 10 different shops in India: {apple_price_india}")
apple_price_india_cv = statistics.stdev(apple_price_india)/statistics.mean(apple_price_india)
print(f"population cv: {apple_price_india_cv}")

if sample_cv == apple_price_india_cv:
    print(f"Both the sample dataset have {Fore.LIGHTGREEN_EX}same{Style.RESET_ALL} variability")
else:
    print(f"Both the sample dataset have {Fore.LIGHTRED_EX}different{Style.RESET_ALL} variability")
