#!/bin/python3

import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

file_path = "data.csv"
data_frame = pd.read_csv(file_path)
print(data_frame.head())
print(data_frame.describe())


target = data_frame['Admitted'].map({"Yes":1, "No":0})
inputs = data_frame['SAT']
plt.scatter(inputs,target)
plt.show()


sm.add_constant(inputs)
logistic_regression = sm.Logit(target, inputs).fit()
print(logistic_regression.summary())