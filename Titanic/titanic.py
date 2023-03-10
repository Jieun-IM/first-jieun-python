import string
import numpy as np
import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', 100)
pd.set_option('display.max_rows', 10)
pd.set_option('display.width', 100)

from scipy import stats
from statsmodels.stats.weightstats import ztest
import plotly.graph_objs as go
import plotly.express as px
from itertools import cycle
import matplotlib.pyplot as plt
import pandas_profiling

from autoviz.AutoViz_Class import AutoViz_Class
from IPython.display import display
from itertools import cycle
import ppscore as pps
import os
print("")
for dirname, _, filenames in os.walk("C:\data\Pandas - Titanic Project\data\input"):
    for filename in filenames:
        print(os.path.join(dirname, filename))
        
        
df = pd.read_csv("C:\data\Pandas - Titanic Project\data\input\train.csv")
display(df.head())

report = pandas_profiling.ProfileReport(df)
display(report)
report.to_file(out_file="C:\data\Pandas - Titanic Project\data\Profiling_Report.html")
AV = AutoViz_Class()
report_2 = AV.AutoViz('C:\data\Pandas - Titanic Project\data\input\train.csv')
df_survivors = df(df['Survived'] == 1)
df_nonsurvivors = df(df['Survived'] == 0)
violin_survivors = go.Violin(
    y = df_survivors['Age'],
    x = df_survivors['Survived'],
    name = 'Survivors',
    marker_color = 'forestgreen',
    box_visible=True)

violin_nonsurvivors = go.Violin(
    y = df_nonsurvivors['Age'],
    x = df_nonsurvivors['Survived'],
    name = 'Non-Survivors',
    marker_color = 'darked',
    box_visible=True)

data = [violin_nonsurvivors, violin_survivors]

layout = go.Layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    title='"Age" of survivors vs Ages of non-survivors',
    xaxis=dict(
        title='Survived or not'
    ),
    yaxis=dict(
        title='Age'
    )
)

fig = go.Figure(data=data, layout=layout)
fig.show