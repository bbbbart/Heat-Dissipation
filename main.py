import numpy as np
import matplotlib.pyplot as plt

diffusion_rate = 0.1
grid = np.zeros((50, 50), dtype= int)

grid[25,25] = 1

def updateGrid(grid):
    for y, row in enumerate(grid):
        for x, element in enumerate(row):
            delta_temp = 0
            if y != 0:
                delta_temp += element + diffusion_rate * (grid[y - 1, x] - element)
            if y != 49:
                delta_temp += element + diffusion_rate * (grid[y + 1, x] - element)
            if x != 0:
                delta_temp += element + diffusion_rate * (grid[y, x - 1] - element)
            if y != 49:
                delta_temp += element + diffusion_rate * (grid[y, x + 1] - element)
            grid[y,x] += delta_temp
    return grid

plt.imshow(grid, cmap='viridis', interpolation='nearest')
plt.colorbar()
plt.show()