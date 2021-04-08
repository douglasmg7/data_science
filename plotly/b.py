#!/usr/bin/env python
import pandas as pd
import numpy as np

pd.options.plotting.backend = "plotly"

df = pd.DataFrame(np.random.randn(100, 4), columns='A B C D'.split())
df2 = pd.DataFrame({'Category': ['A', 'B', 'C'], 'Values': [32, 43, 50]})
df3 = pd.DataFrame({'x': [1,2,3,4,5], 'y':[10,20,30,20,10],'z':[500,400,300,200,100]})

#  fig = df.plot()

#  fig = df.plot(kind='scatter', x='A', y='B')

#  fig = df2.plot(kind='bar', x='Category', y='Values')

#  fig = df.sum().plot(kind='bar')
#  fig = df.sum().plot.bar()

#  fig = df.plot.box()

#  fig = df['A'].plot.hist()

fig = df[['A', 'B']].plot(kind='hist')

fig.show()