#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 100)
y = x*2
z = x**2

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12,2))
axes[0].plot(x, y, 'b', lw=4)
axes[0].set_xlabel('X')
axes[0].set_ylabel('Y')

axes[1].plot(x, z, 'r', lw=3, ls='--')
axes[1].set_xlabel('X')
axes[1].set_ylabel('Z')

plt.show()
