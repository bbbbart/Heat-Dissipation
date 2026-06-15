import numpy as np
from main import image, ax

grid = np.zeros((25, 25))
ghost_grid = np.zeros((27,27))
diffusion_rate = 0.1
pause = False

def resetGrid():
   grid.fill(0)
   ghost_grid.fill(0)

def updateGrid(frame):
    if not pause:
      global grid

      ghost_grid[1:-1, 1:-1] = grid ## makes center of ghost grid equal to grid
      ghost_grid[0::len(ghost_grid)-1, 1:-1] =  grid[0::len(grid)-1]  ## makes top and bottom row of grid equal to ghost grid
      ghost_grid[1:-1, 0::len(ghost_grid)-1] = grid[:, 0::len(grid)-1] ## makes left and right row of grid equal to ghost grid

      up = ghost_grid[:-2, 1:-1]
      down = ghost_grid[2:, 1:-1]
      left = ghost_grid[1:-1, :-2]
      right = ghost_grid[1:-1, 2:]

      total_heat = np.sum(grid)

      grid = grid + diffusion_rate * ((up + down + left + right) - 4 * grid) ## updates center of ghost grid while also using border cells for calculations

      image.set_data(grid)
      ax.set_title(f"Total heat: {total_heat}")
      return(image)
  
    else:
      ax.set_title("(Paused)")
      return(image)