import pandas as pd
# 필터링 예제
weather = pd.read_csv("C:\data\csv\weather.csv", index_col=0, encoding='CP949')
print(weather['최대 풍속(m/s)'] >= 10)

print(weather[weather['최대 풍속(m/s)'] >= 10])

 # 빠진 값 찾고 삭제하기 : .isna()
print(weather['평균 풍속(m/s)'].isna())

missing_data = weather [ weather['평균 풍속(m/s)'].isna() ]
print(missing_data)

# 빠진 값 찾고 삭제하기 : dropna
weather.dropna(axis=0, how="any", inplace=False)
print(weather.loc['2012-02-11'])

# 빠진 데이터를 꺠끗하게 메워 보자 : fillna

weather.fillna(0, inplace=True)
print(weather.loc['2012-02-11'])

# 데이터 구조를 변경 : pivot
df_1 = pd.DataFrame({'item' : ['ring0', 'ring0', 'ring1', 'ring1'],
                     'type' : ['Gold', 'Silver', 'Gold', 'Bronze'],
                     'price' : [20000, 10000, 50000, 30000]})
print(df_1)
df_2 = df_1.pivot(index='item', columns='type', values='price')
print(df_2)