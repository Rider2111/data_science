import matplotlib.pyplot as plt
import pandas as pd
import regression
import numpy as np
import sys;
import statsmodels.api as sm
import logging
import math

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


# Original Scatter Data
plt.subplot(2, 3, 1)
plt.scatter(x_sat, y_gpa)
plt.title("Original scatter data")
plt.xlabel("SAT")
plt.ylabel("GPA")

slope, intercept = regression.get_slope_and_intercept(np.array(x_sat), np.array(y_gpa))
logging.info(f"homemade slope: {slope}, intercept: {intercept}")
homemade_y_gpa = []
for value in x_sat:
    homemade_y_gpa.append(slope * value + intercept)


# Homemade regression
plt.subplot(2, 3, 2)
plt.scatter(x_sat, y_gpa)
plt.plot(x_sat, homemade_y_gpa)
plt.title("Homemade regression")
plt.xlabel("SAT")
plt.ylabel("GPA")


# OLS regression
result = sm.OLS(y_gpa,sm.add_constant(x_sat)).fit()
logging.info(f"OLS summary:\n{result.summary()}")
ols_y_gpa = []
for value in x_sat:
    ols_y_gpa.append(0.0017 * value + 0.2750)

plt.subplot(2,3,3)
plt.scatter(x_sat, y_gpa)
plt.plot(x_sat, ols_y_gpa)
plt.title("OLS Regression")
plt.xlabel("SAT")
plt.ylabel("GPA")


# Sum of Squares Total (SST)
y_gpa_mean = 3.330238
plt.subplot(2,3,4)
plt.scatter(x_sat, y_gpa)
plt.axhline(y_gpa_mean, color='r')
plt.plot([x_sat[x_sat.size/2], x_sat[x_sat.size/2]], [y_gpa_mean, y_gpa[y_gpa.size/2]])
plt.title("Sum of Squares Total (SST)")
plt.xlabel("SAT")
plt.ylabel("GPA")

sst = sum([math.pow(n - y_gpa_mean, 2) for n in y_gpa])
logging.info(f"SST: {sst}")


plt.suptitle("SAT VS GPA")
plt.show()
