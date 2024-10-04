import matplotlib.pyplot as plt
import pandas as pd
import regression
import numpy as np
import sys;
import statsmodels.api as sm
import logging

if len(sys.argv) != 2:
    raise Exception("File path not provided")
logger = logging.getLogger()
logger.setLevel(logging.INFO)

file_path = sys.argv[1]
logging.info(f"Reading data from file: {file_path}")

data_frame = pd.read_csv(file_path)

y_gpa = data_frame["GPA"]
x_sat = data_frame["SAT"]

plt.subplot(1, 3, 1)
plt.scatter(x_sat, y_gpa)
plt.title("Original scatter data")
plt.xlabel("SAT")
plt.ylabel("GPA")

slope, intercept = regression.get_slope_and_intercept(np.array(x_sat), np.array(y_gpa))
logging.info(f"homemade slope: {slope}, intercept: {intercept}")
homemade_y_gpa = []
for value in x_sat:
    homemade_y_gpa.append(slope * value + intercept)

plt.subplot(1, 3, 2)
plt.scatter(x_sat, y_gpa)
plt.plot(x_sat, homemade_y_gpa)
plt.title("Homemade regression")
plt.xlabel("SAT")
plt.ylabel("GPA")

result = sm.OLS(y_gpa,sm.add_constant(x_sat)).fit()
logging.info(f"OLS summary: {result.summary()}")
ols_y_gpa = []
for value in x_sat:
    ols_y_gpa.append(0.0017 * value + 0.2750)

plt.subplot(1,3,3)
plt.scatter(x_sat, y_gpa)
plt.plot(x_sat, ols_y_gpa)
plt.title("OLS Regression")
plt.xlabel("SAT")
plt.ylabel("GPA")

plt.suptitle("SAT VS GPA")
plt.show()
