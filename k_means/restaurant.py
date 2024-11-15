#!/bin/python3

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
sns.set()

data_frame = pd.read_csv('data.csv')

print(data_frame.head())
print(data_frame.describe())
print(data_frame.columns)


income = data_frame["Income"]
avg_spend = data_frame["AverageSpend"]

data = data_frame[['Income', "AverageSpend"]]


k_means = KMeans(10)
model  =k_means.fit(data)
data_frame['cluster_prediction'] = model.fit_predict(data)

plt.scatter(income, avg_spend, c=data_frame['cluster_prediction'], cmap="rainbow")
plt.show()
