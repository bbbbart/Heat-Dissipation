import matplotlib.widgets as widget
import simulation

diffusion_slider_axes = simulation.plt.axes([0.25, 0.075, 0.50, 0.05])
diffusion_slider = widget.Slider(ax = diffusion_slider_axes, 
                          label= 'Thermal Diffusivity', 
                          valmin = 0.01, 
                          valmax = 0.20)

intensity_slider_axes = simulation.plt.axes([0.25, 0.02, 0.5, 0.05])
intensity_slider = widget.Slider(ax = intensity_slider_axes, 
                          label= 'Heat Intensity', 
                          valmin = 100, 
                          valmax = 500)

brush_slider_axes = simulation.plt.axes([0.08, 0.35, 0.05, 0.5])
brush_slider = widget.Slider(ax = brush_slider_axes, 
                          label= 'Brush Size', 
                          valmin = 1, 
                          valmax = 4, orientation = 'vertical', valstep = 1.0)

mode_button_axes = simulation.fig.add_axes([0.05, 0.2, 0.12, 0.06])
mode_button = widget.Button(ax = mode_button_axes, 
                       label = 'Click Mode', 
                       color = 'lightgray', 
                       hovercolor = 'gray')