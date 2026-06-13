import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider

fig, ax = plt.subplots()

diffusion_rate = 0.1
heat_intensity = 0
grid = np.zeros((25, 25))
ghost_grid = np.zeros((27,27))

pause = False

image = ax.imshow(grid, vmin = 0, vmax = 500, cmap='magma', interpolation = 'bilinear')
scale = fig.colorbar(image)
plt.subplots_adjust(bottom = 0.2)
diffusion_slider_axes = plt.axes([0.25, 0.075, 0.50, 0.05])
diffusion_slider = Slider(ax = diffusion_slider_axes, 
                          label= 'Thermal Diffusivity', 
                          valmin = 0.01, 
                          valmax = 0.20)

intensity_slider_axes = plt.axes([0.25, 0.02, 0.50, 0.05])
intensity_slider = Slider(ax = intensity_slider_axes, 
                          label= 'Heat Intensity', 
                          valmin = 50, 
                          valmax = 500)

def addHeat(event):
    if event.inaxes == ax:
      grid[int(event.ydata), int(event.xdata)] += heat_intensity
    image.set_data(grid)

def buttonPresses(event):
    global pause
    if event.key ==  ' ':
      if pause:
        pause = False
      else:
        pause = True
    if event.key == 'r':
       resetGrid()
       
def resetGrid():
   grid.fill(0)
   ghost_grid.fill(0)

fig.canvas.mpl_connect('key_press_event', buttonPresses)
fig.canvas.mpl_connect('button_press_event', addHeat)

def updateDiffusion(val):
   global diffusion_rate
   diffusion_rate = diffusion_slider.val

def updateIntensity(val):
   global heat_intensity
   heat_intensity = intensity_slider.val

diffusion_slider.on_changed(updateDiffusion)
intensity_slider.on_changed(updateIntensity)

def updateGrid(frame):
    while not pause:
      global grid
      global heat_diffusion

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

ani = animation.FuncAnimation(fig, updateGrid, frames = 999, interval = 200)
plt.show()