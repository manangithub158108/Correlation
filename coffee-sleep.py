# importing all the required modules
import csv;
import pandas as pd;
import plotly.express as px;
import numpy as np;

# drawing the graph 
df = pd.read_csv("coffee and sleep.csv");
fig = px.scatter(df, x = 'Coffee in ml', y = 'sleep in hours');
fig.show();

# extracting the coffee and sleep data in thier arrays
sleep = [];
coffee = [];

with open('coffee and sleep.csv') as f:
    reader = csv.reader(f);
    file_data = list(reader);

file_data.pop(0);

for i in range(0, len(file_data)):
    sleep.append(float(file_data[i][2]));
    coffee.append(float(file_data[i][1]));

# printing the coefficient 
correlation = np.corrcoef(sleep, coffee)[0, 1];
print('Correlation coefficient => ' + str(correlation));
