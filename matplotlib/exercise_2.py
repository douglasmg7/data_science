#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 100)
y = x*2
z = x**2

plt.subplot(1, 2, 1)
plt.plot(x, y, 'b', lw=4)

plt.subplot(1, 2, 2,)
plt.plot(x, z, 'r', lw=3, ls='--')

plt.show()

plt.show()
