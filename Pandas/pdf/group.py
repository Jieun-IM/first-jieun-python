import pandas as pd
import datetime as dt

weather = pd.read_csv('C:\data\csv\weather.csv', encoding='CP949')
weather['month'] = pd.DatetimeIndex(weather['일시']).month
means = weather.groupby('month').mean()

print(means)

sum_data = weather.groupby('month').sum()
print(sum_data)