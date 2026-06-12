import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

diffusion_rate = 0.05
grid = np.zeros((25, 25))
ghost_grid = np.zeros((27,27))

pause = False
grid[12,12] = 1500

image = ax.imshow(grid, vmin = 0, vmax = 2000, cmap='magma', interpolation = 'bilinear')
scale = fig.colorbar(image)

def addHeat(event):
    if event.inaxes is not None:
       grid[int(event.ydata), int(event.xdata)] = 1500
       image.set_data(grid)

def buttonPresses(event):
    global pause
    if event.key ==  ' ':
      if pause:
        pause = False
      else:
        pause = True

fig.canvas.mpl_connect('key_press_event', buttonPresses)
fig.canvas.mpl_connect('button_press_event', addHeat)

def updateGrid(frame):
    while not pause:
      global grid
      ghost_grid[1:-1, 1:-1] = grid ## makes center of ghost grid equal to grid
      ghost_grid[0::len(grid[0]), 1:-1] = grid[0::len(grid[0])]   ## makes top and bottom row of grid equal to ghost grid
      ghost_grid[1:-1, 0::len(grid[0])] = grid[:, 0::len(grid[0])] ## makes left and right row of grid equal to ghost grid

      up = ghost_grid[:-2, 1:-1]
      down = ghost_grid[2:, 1:-1]
      left = ghost_grid[1:-1, :-2]
      right = ghost_grid[1:-1, 2:]

      total_heat = np.sum(grid)

      ghost_grid[1:-1, 1:-1] = grid + diffusion_rate * ((up + down + left + right) - 4 * grid) ## updates center of ghost grid while also using border cells for calculations
      grid = ghost_grid[1:-1, 1:-1] ## updates grid

      image.set_data(grid)
      ax.set_title(f"Total heat: {total_heat}")
      return(image)
  
    else:
      ax.set_title("Paused")
      return(image)

ani = animation.FuncAnimation(fig, updateGrid, frames = 100, interval = 100)
plt.show()