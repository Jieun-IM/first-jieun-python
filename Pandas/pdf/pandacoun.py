import pandas as pd
df = pd.read_csv('C:\data\csv\countries.csv')
print(df)
print(type(df))

## index를 0,1,2,3,4가 아닌 원하는 값으로 나타냄 ##
df2 = pd.read_csv('C:\data\csv\countries.csv', index_col= 0)
print(df2)