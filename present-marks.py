# importing all the required modules
import csv;
import pandas as pd;
import plotly.express as px;
import numpy as np;

# drawing the graph 
df = pd.read_csv("present and marks.csv");
fig = px.scatter(df, x = 'Marks In Percentage', y = 'Days Present');
fig.show();

# extracting the coffee and sleep data in thier arrays
marks = [];
present = [];

with open('present and marks.csv') as f:
    reader = csv.reader(f);
    file_data = list(reader);

file_data.pop(0);

for i in range(0, len(file_data)):
    present.append(float(file_data[i][2]));
    marks.append(float(file_data[i][1]));

# printing the coefficient 
correlation = np.corrcoef(marks, present)[0, 1];
print('Correlation coefficient => ' + str(correlation));
