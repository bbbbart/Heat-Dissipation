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

The spread of heat can be modeled by using:  $\frac{\partial u}{\partial t} = \alpha \frac{\partial^2 u}{\partial x^2}$, a partial differential equation. Finite difference approximates derivatives by using the distance between certain points, instead of solving the equation at one specific point.

Using finite difference the change in heat at a specific point can be found based on the four adjacent points. Assuming the distance between each point equals 1, the change in heat can be found using:

$\Delta T_{x,y} =\alpha(T_{x+1,y} + T_{x-1,y} + T_{x,y+1} + T_{x,y-1})$

Where $\alpha$ is thermal diffusivity (how quickly heat spreads through a material) and $T_{x,y}$ is the Temperature at a point (x,y).

At each update of the simulation, this equation is used to see how much the temperature at a point should change. Links to resources that break down in depth how that equation can be derived are found at the end of this page.

### Boundary Conditions

The simulation uses an insulated boundary which prevents heat from leaking out. This is done by using an additional 27x27 grid that copies the border of the original grid. Putting both grids on top of each other creates a 2 cell thick border of identical values, which prevents heat from transeferring outside that wall.

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

See release 1.0.0 for link to download under `HeatDissipation.py`

or

Clone repository and download requirements under `requirements.txt`

## More Info
