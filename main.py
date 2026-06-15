import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider
from matplotlib.widgets import Button

fig, ax = plt.subplots()


brush_size = 1

image = ax.imshow(grid, vmin = 0, vmax = 500, cmap='magma', interpolation = 'bilinear')
scale = fig.colorbar(image)
plt.subplots_adjust(bottom = 0.2)






fig.canvas.mpl_connect('key_press_event', buttonPresses)
fig.canvas.mpl_connect('button_press_event', addHeat)
fig.canvas.mpl_connect('motion_notify_event', addHeat)
fig.canvas.mpl_connect('button_release_event', addHeat)
mode_button.on_clicked(changeMode)
diffusion_slider.on_changed(updateDiffusion)
intensity_slider.on_changed(updateIntensity)


ani = animation.FuncAnimation(fig, updateGrid, frames = 999, interval = 200)
plt.show()