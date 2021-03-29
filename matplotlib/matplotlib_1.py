#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np

# Plot x, y using function
x = np.linspace(0, 5, 11)
y = x ** 2
plt.plot(x, y)
plt.xlabel('X label')
plt.ylabel('Y label')
plt.title('Some text')
plt.show()
