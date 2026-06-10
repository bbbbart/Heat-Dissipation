import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

diffusion_rate = 0.1
grid = np.zeros((25, 25))
grid[12,12] = 500
grid[13,12] = 250
grid[11,12] = 250
grid[12,13] = 250
grid[12,11] = 250
grid[11,11] = 250
grid[13,13] = 250
grid[13,11] = 250
grid[11,13] = 250


image = ax.imshow(grid, vmin = 0, vmax = 500, cmap='magma', interpolation = 'bilinear')
scale = fig.colorbar(image)

def updateGrid(frame):
    center = grid[1:-1, 1:-1]
    up = grid[:-2, 1:-1]
    down = grid[2:, 1:-1]
    left = grid[1:-1, :-2]
    right = grid[1:-1, 2:]

    total_heat = np.sum(grid)

    heat_update = np.pad(center + diffusion_rate * ((up + down + left + right) - 4 * center), 1, mode = 'constant') 
    grid = heat_update
    
    image.set_data(grid)
    ax.set_title(f"Total heat: {total_heat}")
    return(image)
    
ani = animation.FuncAnimation(fig, updateGrid, frames = 100, interval = 100)
plt.show()