# Heat Dissipation

This project is a simulation that models the spread of heat in a grid, using finite difference numerical analysis.

## Features

- Grid based heat spead simulation
- Ability to add heat by clicking
- Paint mode
- Change diffusivity rate
- Add differenct amounts of heat

### Heat Spread

The amound of heat that spreads from one point to another depends on the difference in temperature between them. More heat spreads from two points that have a difference of 50 C rather than two points with a difference of 5 C. After enough has passed, each point will end up having the same temperature, which stops more heat from being transferred
### Numerical Analysis

The spread of heat can be modeled by using:  $\frac{\partial u}{\partial t} = \alpha \frac{\partial^2 u}{\partial x^2}$, a partial differential equation. Finite difference approximates derivatives by using the distance between certain points, instead of solving the equation at one specific point.

Using finite difference the change in heat at a specific point can be found based on the four adjacent points. Assuming the distance between each point equals 1, the change in heat can be found using:

$\Delta T_{x,y} =\alpha(T_{x+1,y} + T_{x-1,y} + T_{x,y+1} + T_{x,y-1})$

Where $\alpha$ is thermal diffusivity (how quickly heat spreads through a material) and $T_{x,y}$ is the Temperature at a point (x,y).

At each update of the simulation, this equation is used to see how much the temperature at a point should change. Links to resources that break down in depth how that equation can be derived are found at the end of this page.

### Boundary Conditions

The simulation uses an insulated boundary which prevents heat from leaking out.

### UI

## Requirements and Running

See release 1.0.0 for link to download under `HeatDissipation.py`

or

Clone repository and download requirements under `requirements.txt`

## More Info
