import pandas as pd
import numpy as np
rains_in_seattle = pd.read_csv("C:\data\seattle2014.csv")
rains_arr = rains_in_seattle['PRCP'].values
print('Data Size:', len(rains_arr))

days_arr = np.arange(0, 365)
condition_jan = days_arr < 31
print(condition_jan[:40])
rains_jan = rains_arr[condition_jan]
print(len(rains_jan))
print(np.sum(rains_jan))
print(np.mean(rains_jan))