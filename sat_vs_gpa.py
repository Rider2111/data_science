#!/bin/python3

import matplotlib.pyplot as plt
import pandas as pd
import regression
import numpy as np
import sys;

if len(sys.argv) != 2:
    raise Exception("File path not provided")

file_path = sys.argv[1]
print(f"Reading data from file: {file_path}")

data_frame = pd.read_csv(file_path)

y_gpa = data_frame["GPA"]
x_sat = data_frame["SAT"]

plt.subplot(1, 2, 1)
plt.scatter(x_sat, y_gpa)
plt.title("Original scatter data")
plt.xlabel("SAT")
plt.ylabel("GPA")

slope, intercept = regression.get_slope_and_intercept(np.array(x_sat), np.array(y_gpa))
new_y_gpa = []
for value in x_sat:
    new_y_gpa.append(slope * value + intercept)

plt.subplot(1, 2, 2)
plt.scatter(x_sat, y_gpa)
plt.plot(x_sat, new_y_gpa)
plt.title("Homemade regression")
plt.xlabel("SAT")
plt.ylabel("GPA")

plt.suptitle("SAT VS GPA")

plt.show()
