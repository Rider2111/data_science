#!/bin/python3

import math

'''
If 2 variables are correlated then we measure the correlation with the help of covariance.
variance is always +ve, but covariance can be +ve, 0, or -ve
Sxy for sample and Sigmaxy for population

+ve: 2 varaibles moves together. If one goes up the other goes up as well
-ve: 2 varaible moves in opposite direction. If one goes up the other goes down
0: 2 variables are independent of each other

Correlation computed value can be anything 0.0234, 123, 343289.32
to properly interpret correlation we need correlation coefficient

correlation of x and y is same as correlation of y and x
'''

house_price = [110, 245, 330, 442, 502]
house_size = [1250, 1955, 2233, 3440, 3990]
n = len(house_price)

house_price_mean = sum(house_price)/n
print(f"House price mean: {house_price_mean}")
house_size_mean = sum(house_size)/n
print(f"House size mean: {house_size_mean}")

# Sample covariance
s_xy = sum((x-house_price_mean)*(y-house_size_mean) for x, y in zip(house_price, house_size))/(n-1)

print(f"Sample covariance: {s_xy}")

'''
correlation coefficient
    correlation(x,y)/(std(x)*std(y))

correlation coefficient value ranges from -1 <= correlation coefficient <= 1
'''

std_house_price = math.sqrt(sum([math.pow(x-house_price_mean, 2) for x in house_price])/(n-1))
print(f"House price std: {std_house_price}")
std_house_size = math.sqrt(sum([math.pow(x-house_size_mean, 2) for x in house_size])/(n-1))
print(f"House size std: {std_house_size}")

print(f"Correlation coefficient: {s_xy/(std_house_price*std_house_size)}")
