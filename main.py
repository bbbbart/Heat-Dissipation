import matplotlib.animation as animation
import user_inputs as ui
import widgets
import simulation

## connects widgets to functions and creates animation

def main():
    simulation.fig.canvas.mpl_connect('key_press_event', ui.buttonPresses)
    simulation.fig.canvas.mpl_connect('button_press_event', ui.addHeat)
    simulation.fig.canvas.mpl_connect('motion_notify_event', ui.addHeat)
    simulation.fig.canvas.mpl_connect('button_release_event', ui.addHeat)
    
    widgets.mode_button.on_clicked(ui.changeMode)
    widgets.diffusion_slider.on_changed(ui.updateDiffusion)
    widgets.intensity_slider.on_changed(ui.updateIntensity)
    widgets.brush_slider.on_changed(ui.updateBrush)
    widgets.randomize_button.on_clicked(simulation.randomize)

    ani = animation.FuncAnimation(simulation.fig, simulation.updateGrid, frames = 999, interval = 100)
    simulation.plt.show()

if __name__ == "__main__":
    main()