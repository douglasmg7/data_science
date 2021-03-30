#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np

# Plot x, y using function
x = np.linspace(0, 5, 11)
y = x ** 2

# Classes mode instead function mode
fig = plt.figure()
axes = fig.add_axes([0, 0, 1, 1])   # 0 - 1 (0 to 100% of window)  x, y, width, height
#  axes.set_title('Some title')
#  axes.set_xlabel('X label')
#  axes.set_ylabel('Y label')

axes.plot(x, 
        y, 
        color='purple', 
        linewidth=3, 
        alpha=.5, 
        linestyle='-.', 
        marker='o', 
        markersize=20, 
        markerfacecolor='yellow', 
        markeredgecolor='green',
)
#  axes.plot(x, y, color='green', linewidth=3, alpha=.5, linestyle='-.', marker='*')
#  axes.plot(x, y, color='green', lw=3, alpha=.5, ls='-.')
#  axes.plot(x, y, color='#FF8C00')     # RGB

# Avoid overlapp axes
#  plt.tight_layout()
#  plt.savefig('my_picture.jpg', dpi=200)
plt.show()
