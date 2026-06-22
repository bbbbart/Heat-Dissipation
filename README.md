# Heat Dissipation

<img width="782" height="590" alt="Recording 2026-06-22 165337" src="https://github.com/user-attachments/assets/df90ca92-19d2-4646-9b82-0d74950be0ae" />

This project uses NumPy and finite difference numerical analysis to model the spread and dissipation of heat throughout a grid.

## Features

- 25x25 grid-based heat diffusion simulation
- Click and paint mode for adding heat
- Adjustable thermal diffusivity and brush size
- Insulated boundary
- Visual grid using Matplotlib

Heat always spreads from a higher temperature region to a lower temperature region. The speed at which heat spreads depends on the difference in temperature between the two regions. Heat transfers faster the greater the difference between the temperatures. This transfer happens until equilibrium, when heat is distributed equally.

### Numerical Analysis

This can be modeled by using the partial differential heat equation, which solves for the rate at which heat transfers:  

### $\frac{\partial u}{\partial t} = \alpha (\frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2})$

A way of approximating the solutions to this equation is by using finite difference. Finite difference approximates derivatives by using the distance between certain points. The form of finite difference this code uses is called FTCS (forward-time-centered scheme). In this method, future states are approximated based on the current state, and the second derivative is approximated by using neighboring points in the x and y directions. By using this to approximate the second derivative in the heat equation, and by assuming that $\Delta x = \Delta y = 1$ and a timestep of $\Delta t = 1$, you can get the equation:

### $u_{x, y}^{new} = u_{x,y} + \alpha(u_{x+1, y} + u_{x-1, y} + u_{x, y+1} + u_{x, y-1} - 4u_{x, y})$

Where $\alpha$ is thermal diffusivity (how quickly heat spreads through a material) and $u_{x, y}$ is the temperature at a point (x,y).

At each update of the simulation, this equation is used to see how much the temperature at a point should change. More information on the math behind this can be found in the links at the bottom of this page.

### Boundary Conditions

The simulation uses an insulated boundary which prevents heat from leaking out. This is done by using an additional 27x27 grid and copying the original 25x25 to its center. The value of the border cells of the larger grid is made equal to the border values of the original grid, preventing heat from flowing across the boundary. 

### UI

<img width="793" height="596" alt="Screenshot 2026-06-20 183308" src="https://github.com/user-attachments/assets/02d4977b-3b24-45d0-868e-a6e8a47a7c94" />


The interface features multiple sliders and buttons, including:

#### <u>Mode</u>
Switch between click mode (Add heat to individual cells) and paint mode (Hold and move mouse to add heat to a wide area)

#### <u>Brush size</u>
Change the size of area filled while in paint mode.

#### <u>Thermal Diffusivity</u>
Choose how quickly the heat spreads through the grid. Thermal diffusivity is limited to a range that keeps the simulation stable.

#### <u>Heat Intensity</u>
How much heat to add in each cell while clicking.

#### <u>Randomize</u>
Add heat in a random pattern to 35% of cells.

## Requirements and Running

Download the latest release and run the executable `HeatDissipation.exe`.

## More Info
[Heat Equation](https://en.wikipedia.org/wiki/Heat_equation)

[Finite Difference Approximations of Derivatives](https://www.dam.brown.edu/people/alcyew/handouts/numdiff.pdf)

[FTCS Scheme in a 2D Heat Equation](https://www.scirp.org/journal/paperinformation?paperid=143957)
