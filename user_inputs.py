import simulation
import widgets

## all functions related to widgets and keyboard buttons

hold = False 
heat_intensity = 100
brush_size = 1
mode = True ## if in paint mode (False) or click mode (True)

def buttonPresses(event):
    if event.key ==  ' ':
      simulation.pause = not simulation.pause
    elif event.key == 'r':
      simulation.resetGrid()

def changeMode(event):
   global mode
   if mode:
      mode = False
      widgets.mode_button.label.set_text('Mode: Paint')
   else:
      mode = True
      widgets.mode_button.label.set_text('Mode: Click')

def addHeat(event):
  global hold
  if event.inaxes == simulation.ax: ## checks if the event is out of bounds
    if event.name == 'button_release_event': ## checks if mouse is being held down
      hold = False
    elif event.name == 'button_press_event':
      hold = True
    if event.name == 'button_press_event': ## adds heat if mouse is clicked
      simulation.grid[int(event.ydata), int(event.xdata)] += heat_intensity
    elif event.name == 'motion_notify_event' and hold and not mode: ## adds heat if mouse is pressed, in motion, and in paint mode
      if brush_size == 1:
        simulation.grid[int(event.ydata), int(event.xdata)] += heat_intensity
      else:
        simulation.grid[int(event.ydata)-brush_size: int(event.ydata)+brush_size,
          int(event.xdata)-brush_size: int(event.xdata)+brush_size] += heat_intensity
        
  simulation.img.set_data(simulation.grid)

def updateDiffusion(val):
   simulation.diffusion_rate = widgets.diffusion_slider.val

def updateIntensity(val):
    global heat_intensity 
    heat_intensity = widgets.intensity_slider.val

def updateBrush(val):
    global brush_size
    brush_size = int(widgets.brush_slider.val)