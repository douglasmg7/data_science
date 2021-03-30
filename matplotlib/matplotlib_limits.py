#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np

# Plot x, y using function
x = np.linspace(0, 5, 11)
y = x ** 2

# Classes mode instead function mode
fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, .8, .8])   # 0 - 1 (0 to 100% of window)  x, y, width, height

ax.plot(x, y, color='purple', lw=2, ls='--')
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
plt.show()
