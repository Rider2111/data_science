#!/bin/python3

import pandas as pd
import sys
import logging
import seaborn as sns
import matplotlib.pyplot as plt
sns.set()
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

if len(sys.argv) != 2:
    raise Exception("File path not provided")

logging.basicConfig(
    filename="output.log",
    filemode='w',
    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
    datefmt='%H:%M:%S',
    level=logging.DEBUG
)

logger = logging.getLogger()
logger.setLevel(logging.INFO)

file_path = sys.argv[1]
logging.info(f"Reading data from file: {file_path}")

data_frame = pd.read_csv(file_path)
logging.info(f"Data frame head:\n{data_frame.head()}")
logging.info(f"Data frame describe:\n{data_frame.describe(include='all')}")

# Preprocessing

## Dropped column model
data_frame = data_frame.drop(['Model'], axis=1) 

logging.info(f"Missing value percentage: {(100/data_frame.size)*sum(data_frame.isnull().sum())}")
data_frame = data_frame.dropna(axis=0)

# sns.displot(data_frame['Price'])

data_frame = data_frame[data_frame['Price'] < data_frame['Price'].quantile(0.99)]
# sns.displot(data_frame['Price'])
# plt.show()

data_frame = data_frame[data_frame['Mileage'] < data_frame['Mileage'].quantile(0.99)]
data_frame = data_frame[data_frame['EngineV'] < 6.5]
data_frame = data_frame[data_frame['Year'] > data_frame['Year'].quantile(0.01)]

data_frame = data_frame.reset_index(drop=True)
logging.info(f"Pre proccessed data frame describe:\n{data_frame.describe()}")


# Regression
data_frame = pd.get_dummies(data_frame, drop_first=True)
target = data_frame["Price"]
inputs = data_frame.drop(["Price"], axis=1)
scaler = StandardScaler()
scaler.fit(inputs)
inputs_scaled = scaler.transform(inputs)
x_train, x_test, y_train, y_test = train_test_split(inputs_scaled, target, test_size=0.2, random_state=365)


regression = LinearRegression()
regression.fit(x_train, y_train)
y_hat = regression.predict(x_train)
logging.info(y_hat)

plt.scatter(y_hat, y_train)
plt.show()