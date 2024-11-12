import sys
import pandas as pd
import logging
import matplotlib.pyplot as plt
from regression import get_slope_and_intercept
import numpy as np
import statsmodels.api as sm
import math

#initial
if len(sys.argv) != 2:
    raise Exception("File path not provided")
logger = logging.getLogger()
logger.setLevel(logging.INFO)

file_path = sys.argv[1]
data_frame = pd.read_csv(file_path)
x_re_size = data_frame['size']
y_re_price = data_frame['price']
y_re_price_mean =  292289.470160

logging.info(f'Data Frame Describe:\n{data_frame.describe()}')

# Original Scatter Data
plt.subplot(3,1,1)
plt.scatter(x_re_size,y_re_price)
plt.xlabel('Size')
plt.ylabel('Price')
plt.title('Original Scatter Data')


# Homemade Regression
slope , intercept = get_slope_and_intercept(np.array(x_re_size), np.array(y_re_price))
logging.info(f"homemade slope: {slope}, intercept: {intercept}")
homemade_y_re_price = []
for value in x_re_size:
    homemade_y_re_price.append(slope * value + intercept)

plt.subplot(3,1,2)
plt.scatter(x_re_size,y_re_price)
plt.plot(x_re_size,homemade_y_re_price,'r')
plt.axhline(y_re_price_mean, color = 'g')
plt.xlabel('Size')
plt.ylabel('Price')
plt.title('Homemade Regression')


# OLS Regression
result = sm.OLS(y_re_price, sm.add_constant(x_re_size)).fit()
logging.info(f"OLS Summary:\n{result.summary()}")
ols_y_re_price = []
for value in x_re_size:
    ols_y_re_price.append(223.1787*value + 1.019e+05)

plt.subplot(3,1,3)
plt.scatter(x_re_size,y_re_price)
plt.plot(x_re_size,ols_y_re_price,'r')
plt.axhline(y_re_price_mean, color = 'g')
plt.xlabel('Size')
plt.ylabel('Price')
plt.title('OLS Regression')

# Sum of Squared Total (SST)
sst = sum([math.pow(n-y_re_price_mean,2) for n in y_re_price])
logging.info(f"Sum of Squares Total (SST): {sst}")

# Sum of Squared Regression (SSR)
ssr = sum(math.pow(n - y_re_price_mean, 2) for n in homemade_y_re_price)
logging.info(f"Sum of Squares Regression (SSR): {ssr}")

# Sum of Squares Error (SSE)
sse = sum(math.pow(homemade_y_re_price[n] - y_re_price[n],2) for n in range(0,len(y_re_price)))
logging.info(f"Sum of Squares Error (SSE): {sse}")

logging.info(f"SST = SSR + SSE : {sst} = {ssr + sse}")

logging.info(f'R^2 = ssr/sst : R^2 = {ssr/sst}')


plt.suptitle('Real Estate Size vs Price')
plt.show()