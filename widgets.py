diffusion_slider_axes = plt.axes([0.25, 0.075, 0.50, 0.05])
diffusion_slider = Slider(ax = diffusion_slider_axes, 
                          label= 'Thermal Diffusivity', 
                          valmin = 0.01, 
                          valmax = 0.20)

intensity_slider_axes = plt.axes([0.25, 0.02, 0.5, 0.05])
intensity_slider = Slider(ax = intensity_slider_axes, 
                          label= 'Heat Intensity', 
                          valmin = 50, 
                          valmax = 500)

mode_button_axes = fig.add_axes([0.05, 0.2, 0.12, 0.06])
mode_button =  Button(ax = mode_button_axes, 
                       label = 'Click Mode', 
                       color = 'lightgray', 
                       hovercolor = 'gray')