from ortools.linear_solver import pywraplp
import numpy as np
import csv
import argparse


# Create a linear solver using the GLOP backend
solver = pywraplp.Solver.CreateSolver('GLOP')


def solve_projects(projects, students, choice_matrix, project_caps):
    """
        Solve the optimal project assignment problem using linear programming.

        Args:
            projects (int): The number of projects available.
            students (int): The number of students.
            choice_matrix (list): A 2D matrix representing the students' project preferences.
                                  Shape: (students, projects)
            project_caps (list): A 1D list representing the maximum number of students allowed for each project.
                                 Shape: (projects,)

        Returns:
            tuple: A tuple containing two elements:
                   - A 2D matrix representing the assignment of students to projects.
                     Shape: (students, projects)
                   - The objective value of the optimized assignment.

        Raises:
            AssertionError: If the input shapes are not valid or if there are not enough project spots for all students.

        Notes:
            - The choice matrix should have shape (students, projects), where each entry represents the preference of a
              student for a particular project.
            - The project caps list should have shape (projects,), where each entry represents the maximum number of students
              allowed for a specific project.

        Example:
            # Example usage
            choice_matrix = [[2, 1, 3], [1, 3, 2], [3, 2, 1]]
            project_caps = [2, 2, 2]
            assignments, objective_value = solve_projects(3, 3, choice_matrix, project_caps)
        """
    assert np.array(choice_matrix).shape == (students, projects), 'Choice matrix must be of shape (students, projects)'
    assert np.array(project_caps).shape == (projects,), 'Project caps must be of shape (projects,)'
    assert np.sum(project_caps) >= students, 'There must be enough project spots for all students'

    x = [[solver.BoolVar(f'x_{i}_{j}') for j in range(projects)] for i in range(students)]
    c = choice_matrix
    t = project_caps

    # Ensure each student is assigned to exactly one project
    for i in range(students):
        total = None
        for j in range(projects):
            if total is None:
                total = x[i][j]
            else:
                total = total + x[i][j]
        solver.Add(total == 1)

    # Ensure that each project has at most t_j students
    for j in range(projects):
        total = None
        for i in range(students):
            if total is None:
                total = x[i][j]
            else:
                total = total + x[i][j]
        solver.Add(total <= t[j])

    # Set the objective function
    objective = solver.Objective()
    for i in range(students):
        for j in range(projects):
            objective.SetCoefficient(x[i][j], c[i][j])
    objective.SetMaximization()

    # Solve the problem
    status = solver.Solve()

    assert status == pywraplp.Solver.OPTIMAL, 'The problem does not have an optimal solution.'

    return [[x[i][j].solution_value() for j in range(projects)] for i in range(students)], objective.Value()


def solve_projects_from_csv(capacity_file, preference_file):
    """
    Solve the optimal project assignment problem using linear programming by loading data from separate CSV files.

    Args:
        capacity_file (str): The path to the CSV file containing the project capacities.
                             The CSV file should have one row representing the project capacities.
        preference_file (str): The path to the CSV file containing the students' preferences.
                               The CSV file should have rows representing the project preferences of each student.

    Returns:
        tuple: A tuple containing two elements:
               - A 2D matrix representing the assignment of students to projects.
               - The objective value of the optimized assignment.

    Raises:
        FileNotFoundError: If any of the provided file paths do not exist.
        AssertionError: If the CSV file formats are incorrect.

    Example:
        # Example usage
        capacity_file = 'capacity.csv'
        preference_file = 'preferences.csv'
        assignments, objective_value = solve_projects_from_csv(capacity_file, preference_file)
    """
    # Load project capacities from CSV
    try:
        with open(capacity_file, 'r') as file:
            reader = csv.reader(file)
            capacity_row = next(reader)  # Read the first row
            project_caps = [int(capacity) for capacity in capacity_row]
            assert len(project_caps) > 0, "Project capacities should be provided."
    except FileNotFoundError:
        raise FileNotFoundError("Capacity file not found.")
    except (ValueError, IndexError, AssertionError):
        raise AssertionError("Invalid capacity CSV file format.")

    # Load student preferences from CSV
    try:
        with open(preference_file, 'r') as file:
            reader = csv.reader(file)
            choice_matrix = [[int(choice) for choice in row] for row in reader]
            assert all(len(row) == len(project_caps) for row in choice_matrix), "Choice matrix shape does not match project capacities."
    except FileNotFoundError:
        raise FileNotFoundError("Preference file not found.")
    except (ValueError, IndexError, AssertionError):
        raise AssertionError("Invalid preference CSV file format.")

    # Call solve_projects with the loaded data
    return solve_projects(len(project_caps), len(choice_matrix), choice_matrix, project_caps)


if __name__ == '__main__':
    # Get file paths from arguments
    parser = argparse.ArgumentParser(description='Solve the optimal project assignment problem using linear programming.')
    parser.add_argument('capacity_file', type=str, help='The path to the CSV file containing the project capacities.')
    parser.add_argument('preference_file', type=str, help='The path to the CSV file containing the students\' preferences.')
    args = parser.parse_args()

    # Solve the problem
    assignments, objective_value = solve_projects_from_csv(args.capacity_file, args.preference_file)
    print(f'Assignments:\n{np.array(assignments)}')
    print(f'Objective value: {objective_value}')

    # Save the assignments to a CSV file
    np.savetxt('assignments.csv', assignments, delimiter=',', fmt='%d')

    # Save the objective value to a text file
    with open('objective_value.txt', 'w') as file:
        file.write(str(objective_value))

    print('Saved assignments to assignments.csv and objective value to objective_value.txt')