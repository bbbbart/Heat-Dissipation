import numpy as np
import matplotlib.pyplot as plt

## functions related to calculations and grid updating

grid = np.zeros((25, 25)) ## main grid
ghost_grid = np.zeros((27,27)) ## additional grid to do calculations at boundaries
diffusion_rate = 0.1 
pause = False
total_heat = 0
rng = np.random.default_rng(16) ## creates random generator

fig, ax = plt.subplots()
fig.set_size_inches(8,6)
img = ax.imshow(grid, vmin = 0, vmax = 500, cmap='magma', interpolation = 'bilinear') ## creates heatmap
scale = fig.colorbar(img)
plt.subplots_adjust(bottom = 0.2)
fig.canvas.manager.set_window_title("Heat Dissipation")
plt.text(26.5, 30.5, "Keyboard Functions: \nR = reset \nSpace = pause", fontsize = 10, fontweight = 'bold') 


def resetGrid():
  global total_heat
  grid.fill(0)
  ghost_grid.fill(0)
  total_heat = 0
  img.set_data(grid)

def randomize(event):
  global grid
  r = rng.random((len(grid),len(grid))) ## 25x25 grid of random float values
  grid[r> 0.65] = 500
  img.set_data(grid)

def updateGrid(frame):
    global grid, total_heat
    if not pause:
      
      ghost_grid[1:-1, 1:-1] = grid ## makes center of ghost grid equal to grid
      ghost_grid[0::len(ghost_grid)-1, 1:-1] =  grid[0::len(grid)-1]  ## makes top and bottom row of grid equal to ghost grid
      ghost_grid[1:-1, 0::len(ghost_grid)-1] = grid[:, 0::len(grid)-1] ## makes left and right row of grid equal to ghost grid

      up = ghost_grid[:-2, 1:-1] ## all up values
      down = ghost_grid[2:, 1:-1] ## all down values
      left = ghost_grid[1:-1, :-2] ## all left values
      right = ghost_grid[1:-1, 2:] ## all right values

      total_heat = np.sum(grid)

      grid += diffusion_rate * ((up + down + left + right) - 4 * grid) ## updates center of grid while also using ghost grid cells for calculations

      img.set_data(grid)
      ax.set_title(f"Total heat: {total_heat}")
      return(img,)
  
    else:
      ax.set_title(f"(Paused) Total heat: {total_heat}")
      return(img,)