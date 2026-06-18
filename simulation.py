import numpy as np
import matplotlib.pyplot as plt

grid = np.zeros((25, 25))
ghost_grid = np.zeros((27,27))
diffusion_rate = 0.1
pause = False

fig, ax = plt.subplots()
fig.set_size_inches(8,6)
img = ax.imshow(grid, vmin = 0, vmax = 500, cmap='magma', interpolation = 'bilinear')
scale = fig.colorbar(img)
plt.subplots_adjust(bottom = 0.2)

def resetGrid():
  grid.fill(0)
  ghost_grid.fill(0)

def updateGrid(frame):
    global grid
    if not pause:
      
      ghost_grid[1:-1, 1:-1] = grid ## makes center of ghost grid equal to grid
      ghost_grid[0::len(ghost_grid)-1, 1:-1] =  grid[0::len(grid)-1]  ## makes top and bottom row of grid equal to ghost grid
      ghost_grid[1:-1, 0::len(ghost_grid)-1] = grid[:, 0::len(grid)-1] ## makes left and right row of grid equal to ghost grid

      up = ghost_grid[:-2, 1:-1]
      down = ghost_grid[2:, 1:-1]
      left = ghost_grid[1:-1, :-2]
      right = ghost_grid[1:-1, 2:]

      total_heat = np.sum(grid)

      grid += diffusion_rate * ((up + down + left + right) - 4 * grid) ## updates center of ghost grid while also using border cells for calculations

      img.set_data(grid)
      ax.set_title(f"Total heat: {total_heat}")
      return(img,)
  
    else:
      ax.set_title("(Paused)")
      return(img,)