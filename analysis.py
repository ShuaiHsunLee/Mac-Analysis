import pandas as pd

data = pd.read_csv('cpu_info.csv', error_bad_lines=False)

print(data.head())
# print(type(data['PID'].head()), data['PID'].head())