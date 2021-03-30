#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 100)
y = x*2
z = x**2

fig = plt.figure()

ax1 = fig.add_axes([.1, .1, .8, .8])
ax1.set_title('title')
ax1.set_xlabel('X')
ax1.set_ylabel('Z')
ax1.plot(x, z)

ax2 = fig.add_axes([.2, .5, .3, .3])
ax2.set_title('title')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_xlim([20, 22])
ax2.set_ylim([30, 50])
ax2.plot(x, y)

#  plt.plot(x, y)
plt.show()
