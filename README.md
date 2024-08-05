# Pendulum Simulation Projects

Welcome to the Pendulum Simulation Projects repository! This repository contains multiple Python scripts that simulate pendulum dynamics using the Pygame library. These simulations are designed to visualize the behavior of pendulums, including single and double pendulums, as well as variations with small perturbations.

## Table of Contents

- [Projects Overview](#projects-overview)
- [Installation](#installation)
- [Usage](#usage)
- [Project Details](#project-details)
- [Contributing](#contributing)
- [License](#license)

## Projects Overview

This repository includes the following projects:

1. **chaos.py**: Simulates a double pendulum system and visualizes its chaotic behavior by plotting the trajectories of two pendulums with slightly different initial conditions.

2. **chaos3_py**: Extends the double pendulum simulation to include a third pendulum with added error, demonstrating how small changes in initial conditions can lead to divergent behaviors.

3. **double_pendulums.py**: Simulates a double pendulum with user-defined lengths and initial angles, and displays the results along with the pendulum's motion trail.

4. **ten_pendulums.py**: Simulates a system with ten coupled pendulums and visualizes their interactions.

## Installation

To run these simulations, you'll need Python and the Pygame library. Follow these steps to set up your environment:

1. Clone this repository:

    ```bash
    git clone https://github.com/parthvs/Double-pendulum.git
    cd Double-pendulum
    ```

2. Install the required packages:

    ```bash
    pip install pygame
    ```

## Usage

Run each script with Python to start the simulation. For example:

- For **chaos.py**:

    ```bash
    python chaos.py
    ```

- For **chaos3_py**:

    ```bash
    python chaos3_py.py
    ```

- For **double_pendulums.py**:

    ```bash
    python double_pendulums.py
    ```

- For **ten_pendulums.py**:

    ```bash
    python ten_pendulums.py
    ```

Follow the prompts and instructions provided by each script to interact with the simulations.

## Project Details

### chaos.py

- **Description**: Simulates the chaotic behavior of a double pendulum.
- **Key Features**:
  - Visualizes the paths of two pendulums with slightly different initial conditions.
  - Demonstrates the sensitivity to initial conditions.

### chaos3_py

- **Description**: Extends the double pendulum simulation to include a third pendulum with small perturbations.
- **Key Features**:
  - Visualizes the impact of small changes in initial conditions on the system's behavior.
  - Provides a comparison of three different initial conditions.

### double_pendulums.py

- **Description**: Simulates a double pendulum system with user-defined parameters.
- **Key Features**:
  - Allows users to input pendulum lengths and initial angles.
  - Displays the motion trail and pendulum state information.

### ten_pendulums.py

- **Description**: Simulates a system of ten coupled pendulums.
- **Key Features**:
  - Visualizes the complex interactions between multiple pendulums.



Happy simulating!
