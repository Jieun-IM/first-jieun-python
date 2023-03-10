import pandas as pd

df = pd.DataFrame({
    'name' : ['A', 'B', 'C', 'D'],
    'horse power' : [120, 220, 120, 200],
    'weight' : [1.9, 2.1, 1.5, 2.9],
    'efficiency' : [18.3, 19.2, 21.1, 17.3]})

# 1)
new_df = df.set_index(['name'])
print(new_df)

 # 2)
df_1 = pd.DataFrame({
   'name' : ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'horse power' : [130, 250, 190, 300, 210, 220, 170],
    'weight' : [1.9, 2.6, 2.2, 2.9, 2.4, 2.3, 2.2],
    'efficiency': [16.3, 10.2, 11.1, 7.1, 12.1, 13.2, 14.2] })
df_3 = pd.concat([df_1, df])

df_3 = df_3.set_index('name')
print(df_3)

# 3)
df_1['com'] = 'P'

df['com'] = 'Q'
df_4 = pd.concat([df_1, df])
df_4 = df_4.set_index('name')
print(df_4)

# 4)
df_4['hp x mile'] = df_4['horse power'] * df_4['efficiency']
print(df_4.groupby('com').mean()['hp x mile'])