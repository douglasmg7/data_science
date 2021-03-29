#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np

# Plot x, y using function
x = np.linspace(0, 5, 11)

# Classes mode instead function mode
# 3 x 2 plots
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(3,2), dpi=100)
axes[0].set_title('Plot 1')
axes[0].set_xlabel('X')
axes[0].set_ylabel('Y')
axes[0].plot(x, x ** 2)
axes[1].set_title('Plot 2')
axes[1].set_xlabel('X')
axes[1].set_ylabel('Y')
axes[1].plot(x, x ** 3)
# Avoid overlapp axes
plt.tight_layout()
plt.show()


