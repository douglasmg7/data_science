#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np

# Plot x, y using function
x = np.linspace(0, 5, 11)
y = x ** 2

# Sub plot - Several graphics - (nrows, ncols, index)
plt.subplot(1, 2, 1)
plt.plot(x, y, 'r')
plt.subplot(1, 2, 2)
plt.plot(y, x, 'b')
plt.show()
