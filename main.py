import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

diffusion_rate = 0.1
grid = np.zeros((25, 25))
ghost_grid = np.zeros((27,27))
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
    global grid

    ghost_grid[1:-1, 1:-1] = grid
    ghost_grid[0::len(grid[0]), 1:-1] = grid[0::len(grid[0])]
    ghost_grid[1:-1, 0::len(grid[0])] = grid[:, 0::len(grid[0])]

    up = ghost_grid[:-2, 1:-1]
    down = ghost_grid[2:, 1:-1]
    left = ghost_grid[1:-1, :-2]
    right = ghost_grid[1:-1, 2:]

    total_heat = np.sum(grid)

    ghost_grid[1:-1, 1:-1] = grid + diffusion_rate * ((up + down + left + right) - 4 * grid)
    grid = ghost_grid[1:-1, 1:-1]

    image.set_data(grid)
    ax.set_title(f"Total heat: {total_heat}")
    return(image)
    
ani = animation.FuncAnimation(fig, updateGrid, frames = 100, interval = 100)
plt.show()