from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import f_regression
from sklearn.preprocessing import StandardScaler
import pandas as pd
import sys
import logging

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
x_sat_and_rand = data_frame[["SAT","Rand 1,2,3"]]
scaler = StandardScaler()
scaler.fit(x_sat_and_rand)
x_sat_and_rand_scaled = scaler.transform(x_sat_and_rand)

logging.info(f"x_sat_and_rand scaled:\n{x_sat_and_rand_scaled}")


p_value = f_regression(x_sat_and_rand,y_gpa)[1]
p_value = p_value.round(4)
logging.info(f"P value: {p_value}")

reg = LinearRegression()
reg.fit(x_sat_and_rand_scaled,y_gpa)
sklearn_slope = reg.coef_
sklearn_intercept = reg.intercept_
logging.info(f"Coefficients: {sklearn_slope}\nIntercept: {sklearn_intercept}")