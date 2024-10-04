import math
from numpy import ndarray, array
import pandas as pd

def get_slope_and_intercept(xs: ndarray, ys: ndarray):
    if xs.size != ys.size:
        raise Exception(f"Length doesn't match. xs.size: {xs.size}. ys.size: {ys.size}")
    n = xs.size
    sum_x = xs.sum()
    sum_y = ys.sum()
    sum_xy = 0
    sum_x2 = 0
    i = 0
    while (i < xs.size):
        sum_xy += xs[i] * ys[i]
        sum_x2 += math.pow(xs[i], 2)
        i += 1
    m = (n*sum_xy - sum_x*sum_y)/(n*sum_x2 - math.pow(sum_x,2))
    b = (sum_y - m*sum_x)/n
    return (m,b)
