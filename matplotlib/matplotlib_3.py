#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np

# Plot x, y using function
x = np.linspace(0, 5, 11)
y = x ** 2

# Classes mode instead function mode
fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])   # 0 - 1 (0 to 100% of window)  x, y, width, height
axes.set_title('Some title')
axes.set_xlabel('X label')
axes.set_ylabel('Y label')
axes.plot(x, y)
# Avoid overlapp axes
plt.tight_layout()
plt.savefig('my_picture.jpg', dpi=200)
plt.show()
