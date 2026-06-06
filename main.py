import numpy as np
import matplotlib.pyplot as plt

grid = np.zeros((50, 50), dtype= int)

grid[25,25] = 1

plt.imshow(grid, cmap='viridis', interpolation='nearest')
plt.colorbar()
plt.show()