# Math-3020 Computer Project

This project simulates the spread and removal of a computer virus within a network of computers. 
It utilizes the Monte Carlo method to estimate:

* Infection clear time: The average time it takes for the virus to be cleared from the network.
* Probability of infection: The likelihood that a computer will be infected within a given time frame.
* Expected infections: The number of computers expected to be infected under certain conditions.

## Features
* Monte Carlo Simulation: Randomized trials simulate virus behavior over multiple iterations.
* Adjustable Parameters: Probability of infection per computer, infection duration, number of trials, and removal rates can be customized.

## Prerequisites and Required libraries:
* Python 3.x
* numpy
* matplotlib for data visualization

## Results
The simulation outputs:

* Average infection time across multiple runs.
* Probability of infection per computer.
* A summary table showing infection trends over the simulation.
