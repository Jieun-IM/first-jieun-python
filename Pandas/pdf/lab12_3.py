import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

weather = pd.read_csv("C:\data\csv\weather.csv", encoding='CP949')

weather['month'] = pd.DatetimeIndex(weather['일시']).month
means = weather.groupby('month').mean()
means['평균 풍속(m/s)'].plot(kind = 'bar')

plt.show()