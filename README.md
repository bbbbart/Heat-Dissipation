# Heat Dissipation

This project is a simulation that models the spread of heat in a grid, using finite difference numerical analysis.

## Features

- 25x25 grid based heat spead simulation
- Ability to add heat by clicking
- Paint mode
- Change diffusivity rate
- Add differenct amounts of heat

The amound of heat that spreads from one point to another depends on the difference in temperature between them. More heat spreads from two points that have a difference of 50 C rather than two points with a difference of 5 C. After enough has passed, each point will end up having the same temperature, which stops more heat from being transferred
### Numerical Analysis

This can be modeled by using the partial differential Heat Equation, which solves for the rate a which heat transfers:  

### $\frac{\partial u}{\partial t} = \alpha \frac{\partial^2 u}{\partial x^2}$

A way of approximating the solutions to this equation is by using finite difference. Finite difference approximates derivatives by using the distance between certain points. The form of finite difference this code uses is called FTCS (forward-time-centered scheme). In this method, future states are approximated based on the initial state, and the derivative at a point is approximated by using both its forward and backward points on the axis. By using this to approximate the second derivative in the heat equation, and by assuming that $\Delta x = 1$ and each timestep is $t = 1$, you can get the equation:

### $\Delta T_{y}^{x} =\alpha(T_{y}^{x+1} + T_{y}^{x-1} + T_{y+1}^{x} + T_{y-1}^{x})$

Where $\alpha$ is thermal diffusivity (how quickly heat spreads through a material) and $T_{y}^{x}$ is the Temperature at a point (x,y).

At each update of the simulation, this equation is used to see how much the temperature at a point should change. More information on the math behind this can be found at the bottom of this page.

### Boundary Conditions

The simulation uses an insulated boundary which prevents heat from leaking out. This is done by using an additional 27x27 grid that copies the border of the original grid. Putting both grids on top of each other creates a 2 cell thick border of identical values, which prevents heat from transferring outside that wall.

### UI

<img width="793" height="596" alt="Screenshot 2026-06-20 183308" src="https://github.com/user-attachments/assets/02d4977b-3b24-45d0-868e-a6e8a47a7c94" />

The interface features multiple sliders and buttons, including:

#### Mode
Switch between click mode (Add heat to individual cells) and paint mode (Hold and move mouse to add heat to a wide area)

#### Brush size
Change the size of area filled while in paint mode.

#### Thermal Diffusivity
Choose how quickly the heat spreads through the grid.

#### Heat Intensity
How much heat to add in each cell while clicking.

#### Randomize
Add heat in a random pattern, with each cell having a 35% chance.

## Requirements and Running

See release 1.0.0 and download `HeatDissipation.py`. Click the download to run the program.

or

Clone repository and download requirements under `requirements.txt`

## More Info
[Heat Equation](https://en.wikipedia.org/wiki/Heat_equation)

[Finite Difference Approximations of Derivatives](https://www.dam.brown.edu/people/alcyew/handouts/numdiff.pdf)

[FTCS Scheme in a 2D Heat Equation](https://www.scirp.org/journal/paperinformation?paperid=143957)
