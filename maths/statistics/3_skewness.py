#!/bin/python3

import statistics
import matplotlib.pyplot as plt

def get_mean(arr):
    n = len(arr)
    return sum(arr)/n

def get_median(arr):
    n = len(arr)
    if n%2 == 0:
        mid_plus_one_index = int(n/2)
        mid_index = mid_plus_one_index-1
        return (arr[mid_index] + arr[mid_plus_one_index])/2
    mid_index = int(n/2)
    return arr[mid_index]


def get_frequency(arr):
    result = {}
    for element in arr:
        if element in result.keys():
            result[element] = result[element] + 1
        else:
            result[element] = 1
    return result


'''
+ve skew aka right skew
means outliers are to the right
'''
data0 = [1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 5, 5, 7]
freq0 = get_frequency(data0)

print(f"Mean0: {get_mean(data0)}")
print(f"Median0: {get_median(data0)}")
print(f"Freq0: {freq0}")

data1 = [1, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7]
freq1 = get_frequency(data1)

print(f"Mean1: {get_mean(data1)}")
print(f"Median1: {get_median(data1)}")
print(f"Freq1: {freq1}")

plt.subplot(1, 2, 1)
plt.plot(freq0.keys(), freq0.values(), color="r")
plt.title("Right skew")

plt.subplot(1, 2, 2)
plt.plot(freq1.keys(), freq1.values(), color="y")
plt.title("Left skew")
plt.show()
