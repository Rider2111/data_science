import matplotlib.pyplot as plt
import pandas as pd
import regression
import numpy as np
import sys;
import statsmodels.api as sm
import logging
import math
from sklearn.linear_model import LinearRegression

# Inital
if len(sys.argv) != 2:
    raise Exception("File path not provided")
logger = logging.getLogger()
logger.setLevel(logging.INFO)

file_path = sys.argv[1]
logging.info(f"Reading data from file: {file_path}")

data_frame = pd.read_csv(file_path)
logging.info(f"Data frame describe:\n{data_frame.describe()}")

y_gpa = data_frame["GPA"]
x_sat = data_frame["SAT"]
y_gpa_mid = y_gpa[y_gpa.size/2]
x_gpa_mid = x_sat[x_sat.size/2]

# Original Scatter Data
plt.subplot(2, 3, 1)
plt.scatter(x_sat, y_gpa)
plt.title("Original scatter data")
plt.xlabel("SAT")
plt.ylabel("GPA")


# Homemade regression
slope, intercept = regression.get_slope_and_intercept(np.array(x_sat), np.array(y_gpa))
logging.info(f"homemade slope: {slope}, intercept: {intercept}")
homemade_y_gpa = []
for value in x_sat:
    homemade_y_gpa.append(slope * value + intercept)

plt.subplot(2, 3, 2)
plt.scatter(x_sat, y_gpa)
plt.plot(x_sat, homemade_y_gpa, color = 'y')
plt.title("Homemade regression")
plt.xlabel("SAT")
plt.ylabel("GPA")


# SkLearn regression
x_sat_matrix = x_sat.values.reshape(-1,1)
reg = LinearRegression()
reg.fit(x_sat_matrix,y_gpa)
r_squared_value = reg.score(x_sat_matrix,y_gpa)
sklearn_slope = reg.coef_
sklearn_intercept = reg.intercept_
logging.info(f"SkLearn Values\nR-Squared: {r_squared_value}\nSlope: {sklearn_slope}\nIntercept: {sklearn_intercept}")
sklearn_y_gpa = []
for value in x_sat:
    sklearn_y_gpa.append(sklearn_slope * value + sklearn_intercept)

plt.subplot(2,3,3)
plt.scatter(x_sat, y_gpa)
plt.plot(x_sat, sklearn_y_gpa, color = 'y')
plt.title("SkLearn Regression")
plt.xlabel("SAT")
plt.ylabel("GPA")


# Calculation done using homemade regression. OLS removes outliers which leads to invalid calculation
# Sum of Squares Total (SST)
y_gpa_mean = 3.330238
plt.subplot(2,3,4)
plt.scatter(x_sat, y_gpa)
plt.axhline(y_gpa_mean, color='r')
plt.plot([x_gpa_mid, x_gpa_mid], [y_gpa_mean, y_gpa[y_gpa.size/2]], '-g', linewidth = '3')
plt.title("Sum of Squares Total (SST) (Homemade)")
plt.xlabel("SAT")
plt.ylabel("GPA")

sst = sum([math.pow(n - y_gpa_mean, 2) for n in y_gpa])
logging.info(f"Sum of Squares Total (SST) (Homemade): {sst}")


# Sum of Squares Regression (SSR)
plt.subplot(2,3,5)
plt.scatter(x_sat, y_gpa)
plt.axhline(y_gpa_mean, color='r')
plt.plot(x_sat, homemade_y_gpa, color = 'y')
line_mid = slope * x_gpa_mid + intercept
plt.plot([x_gpa_mid, x_gpa_mid], [y_gpa_mean, line_mid], '-g', linewidth = '3')
plt.title("Sum of Squares Regression (SSR) (Homemade)")
plt.xlabel("SAT")
plt.ylabel("GPA")

ssr = sum(math.pow(n - y_gpa_mean, 2) for n in homemade_y_gpa)
logging.info(f"Sum of Squares Regression (SSR) (Homemade): {ssr}")


# Sum of Squares Error (SSE)
plt.subplot(2,3,6)
plt.scatter(x_sat, y_gpa)
plt.plot(x_sat, homemade_y_gpa, color = 'y')
plt.plot([x_gpa_mid, x_gpa_mid], [y_gpa_mid, line_mid], '-g', linewidth = '3')
plt.title("Sum of Squares Error (SSE) (Homemade)")
plt.xlabel("SAT")
plt.ylabel("GPA")

sse = sum(math.pow(homemade_y_gpa[n] - y_gpa[n],2) for n in range(0,len(y_gpa)))
logging.info(f"Sum of Squares Error (SSE) (Homemade): {sse}")

logging.info(f"SST = SSR + SSE : {sst} = {ssr + sse}")

logging.info(f'R^2 = ssr/sst : R^2 = {ssr/sst}')

plt.suptitle("SAT VS GPA")
plt.show()
