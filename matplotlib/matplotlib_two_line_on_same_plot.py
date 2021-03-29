#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np

# Plot x, y using function
x = np.linspace(0, 5, 11)

fig  = plt.figure()
ax = fig.add_axes([0 , 0, 1, 1])
ax.plot(x, x**2, label='X Squared') 
ax.plot(x, x**3, label='X Cubed') 

# Show legend
ax.legend(loc=0)
plt.show()


