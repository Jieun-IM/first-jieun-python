import pandas as pd
weather = pd.read_csv("C:\data\csv\weather.csv", index_col=0, encoding='CP949')

print(weather.describe())

...
print('평균 분석 ---------------------')
print(weather.mean())
print('표준 편차 분석 ---------------------')
print(weather.std())
print('weather.csv 파일이 담고 있는 데이터의 열과 개수 ---------------------')
print(weather.count())
print(weather['최대 풍속(m/s)'].count())
print(weather[['최대 풍속(m/s)', '평균 풍속(m/s)']].mean())