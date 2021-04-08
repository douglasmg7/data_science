#!/usr/bin/env python

import pandas as pd
import numpy as np
#  %matplotlib inline
import plotly.graph_objs as go
from  plotly.offline import plot
import chart_studio.plotly as py
import cufflinks as cf
cf.go_offline()
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

#  import pandas as pd
#  import numpy as np
import matplotlib.pyplot as plt
#  import chart_studio.plotly as py
#  from plotly.offline import plot
#  import cufflinks as cf
#  from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
#  #  from plotly import __version__
#  #  print(__version__)
#  cf.go_offline()


df = pd.DataFrame(np.random.randn(100, 4), columns='A B C D'.split())
#  print(df.head())

df2 = pd.DataFrame({'Caregory': ['A', 'B', 'C'], 'Values': [32, 43, 50]})
#  print(df.head())

#  df.plot()
df.iplot()

plt.show()