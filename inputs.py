hold = False
heat_intensity = 50

def buttonPresses(event):
    global pause
    if event.key ==  ' ':
      if pause:
        pause = False
      else:
        pause = True
    if event.key == 'r':
       resetGrid()

def changeMode(event):
   global mode
   global mode_button
   if mode:
      mode = False
      mode_button.label.set_text('Paint Mode')
   else:
      mode = True
      mode_button.label.set_text('Click Mode')

def addHeat(event):
  global hold
  if event.inaxes == ax:
    if event.name == 'button_release_event':
      hold = False
    elif event.name == 'button_press_event':
      hold = True

    if event.name == 'button_press_event' and mode:
      grid[int(event.ydata), int(event.xdata)] += heat_intensity
    elif event.name == 'motion_notify_event'and hold and not mode:
      grid[int(event.ydata)-brush_size: int(event.ydata)+brush_size,
        int(event.xdata)-brush_size: int(event.xdata)+brush_size] += heat_intensity
    image.set_data(grid)

def updateDiffusion(val):
   global diffusion_rate
   diffusion_rate = diffusion_slider.val

def updateIntensity(val):
   global heat_intensity
   heat_intensity = intensity_slider.val
