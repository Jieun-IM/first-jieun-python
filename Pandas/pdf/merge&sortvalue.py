import pandas as pd
import matplotlib.pyplot as plt
# merge 예제
df_1 = pd.DataFrame({'A': ['a10', 'a11', 'a12'],
                     'B': ['b10', 'b11', 'b12'],
                     'C': ['c10', 'c11', 'c12']}, index = ['가', '나', '다'])

df_2 = pd.DataFrame({'B': ['b23', 'b24', 'b25'],
                     'C': ['c23', 'c24', 'c25'],
                     'D': ['d23', 'd24', 'd25']}, index = ['다', '라', '마'])

df_3 = df_1.merge(df_2, how='outer', on='B')
print(df_3)

# merge에서 인덱스를 키로 사용하는 경우
df_4 = df_1.merge(df_2, how='outer', left_index=True, right_index=True)
print(df_4)

# 데이터를 크기에 따라 나열하기 : sort_values
countries_df = pd.read_csv("C:\data\csv\countries.csv", index_col=0)
sorted = countries_df.sort_values('population')
print(sorted)
