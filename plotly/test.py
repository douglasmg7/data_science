#!/usr/bin/env python

import pandas as pd
import numpy as np
#  %matplotlib inline
import plotly.graph_objs as go
#  from  plotly.offline import plot
from  plotly.offline import _plot_html
import chart_studio.plotly as py
import cufflinks as cf
cf.go_offline()
from plotly.offline import download_plotlyjs, init_notebook_mode, plot,iplot
init_notebook_mode(connected='true')
df = pd.DataFrame(np.random.randn(100,4),columns='A B C D'.split())
df.head()
df.iplot(kind='box')