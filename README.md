# Project Assignment Solver

This project aims to solve the optimal project assignment problem using linear programming techniques. It provides a Python function to find the optimal assignment of students to projects based on their preferences and project capacities.

> ⚠️ The repository might not be up-to-date. Please to the [GitHub repository](https://github.com/NinoDS/project_assignment_solver) for the latest version.
## Prerequisites

- Python 3.7 or higher
- Required packages (see `requirements.txt`)

## Installation

1. Clone the repository:
   ```shell
   git clone https://github.com/NinoDS/project_assignment_solver.git
   ```

2. Navigate to the project directory:
   ```shell
   cd project_assignment_solver
   ```

3. Install the required packages:
   ```shell
   pip install -r requirements.txt
   ```

## Usage

You can use the `solve_projects` function to solve the project assignment problem. It takes the project capacities and student preferences as input and returns the assignment matrix and the objective value.

```python
from ortools.linear_solver import pywraplp
import numpy as np
from project_assignment_solver import solve_projects

# Define project capacities and student preferences
project_caps = [2, 3, 2]
choice_matrix = [[1, 2, 3], [3, 1, 2], [2, 3, 1]]

# Solve the project assignment problem
assignments, objective_value = solve_projects(len(project_caps), len(choice_matrix), choice_matrix, project_caps)

# Print the results
print("Assignments:")
print(assignments)
print("Objective value:", objective_value)
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.