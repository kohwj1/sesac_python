import pandas as pd

data = pd.read_csv('data.csv')
filtered_data = data[data['age'] >= 18]
mean_height = filtered_data['height'].mean()

print('평균 키: ',mean_height)