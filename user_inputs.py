import simulation
import widgets

hold = False
heat_intensity = 50
brush_size = 1
mode = True

def buttonPresses(event):
    if event.key ==  ' ':
      if simulation.pause:
        simulation.pause = False
      else:
        simulation.pause = True
    if event.key == 'r':
       simulation.resetGrid()

def changeMode(event):
   global mode
   if mode:
      mode = False
      widgets.mode_button.label.set_text('Paint Mode')
   else:
      mode = True
      widgets.mode_button.label.set_text('Click Mode')

def addHeat(event):
  global hold
  if event.inaxes == simulation.ax:
    if event.name == 'button_release_event':
      hold = False
    elif event.name == 'button_press_event':
      hold = True

    if event.name == 'button_press_event' and mode:
      simulation.grid[int(event.ydata), int(event.xdata)] += heat_intensity
    elif event.name == 'motion_notify_event'and hold and not mode:
      simulation.grid[int(event.ydata)-brush_size: int(event.ydata)+brush_size,
        int(event.xdata)-brush_size: int(event.xdata)+brush_size] += heat_intensity
    simulation.img.set_data(simulation.grid)

def updateDiffusion(val):
   simulation.diffusion_rate = widgets.diffusion_slider.val

def updateIntensity(val):
    global heat_intensity 
    heat_intensity = widgets.intensity_slider.val
