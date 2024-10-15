import pandas as pd
import sys;
import logging
import matplotlib.pyplot as plt
import statsmodels.api as sm

if len(sys.argv) != 2:
    raise Exception("File path not provided")
logger = logging.getLogger()
logger.setLevel(logging.INFO)

file_path = sys.argv[1]
logging.info(f"Reading data from file: {file_path}")

data_frame = pd.read_csv(file_path)
logging.info(f"Raw data:\n{data_frame}")
logging.info(f"Data frame describe:\n{data_frame.describe()}")

data_frame['Attendance'] = data_frame['Attendance'].map({'Yes':1,'No':0})

y_gpa = data_frame["GPA"]
x_sat = data_frame["SAT"]
plt.scatter(x_sat,y_gpa,c=data_frame['Attendance'],cmap = 'RdYlGn')

x1 = data_frame[['SAT','Attendance']]
x = sm.add_constant(x1)
result = sm.OLS(y_gpa,x).fit()
logging.info(f"OLS Summary:\n{result.summary()}")

y1 = [0.6439 + x*0.0014 for x in x_sat]
y2 = [0.6439 + 0.2226 + x*0.0014 for x in x_sat]
plt.plot(x_sat, y1, color = 'r')
plt.plot(x_sat, y2, color = 'g')
# plt.show()

exp = {
    'const':1,
    'SAT':[1700,1670],
    'Attendance': [0,1]
}
exp_data_frame = pd.DataFrame(exp)
print(result.predict(exp_data_frame))