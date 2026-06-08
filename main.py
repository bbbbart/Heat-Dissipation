import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

diffusion_rate = 0.1
grid = np.zeros(25, 25)
grid[12,12] = 500
grid[13,12] = 500
grid[11,12] = 500
grid[12,13] = 500
grid[12,11] = 500
grid[11,11] = 500
grid[13,13] = 500
grid[13,11] = 500
grid[11,13] = 500

image = ax.imshow(grid, vmin = 0, vmax = 500, cmap='magma', interpolation = 'bilinear')

def updateGrid(frame):
    global grid
    grid_copy = np.copy(grid)
    for y, row in enumerate(grid):
        for x, element in enumerate(row):
            total_temp = 0
            if y != 0:
                total_temp += grid[y - 1, x]
            if y != len(row) - 1:
                total_temp += grid[y + 1, x]
            if x != 0:
                total_temp += grid[y, x - 1]
            if x != len(row) - 1:
                total_temp += grid[y, x + 1]
            grid_copy[y,x] = element + diffusion_rate * (total_temp - (4 * element))
    grid = np.copy(grid_copy)
    image.set_data(grid)
    return(image,)
    

ani = animation.FuncAnimation(fig, updateGrid, frames = 100, interval = 100)
plt.show()
