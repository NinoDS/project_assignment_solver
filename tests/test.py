# Tests

from main import solve_projects


def test_solve_projects():
    """
    Test the `solve_projects` function.
    """
    # Test 1
    students = 4
    projects = 3
    choice_matrix = [[1, 2, 3], [2, 3, 1], [3, 1, 2], [1, 2, 3]]
    project_caps = [2, 2, 2]
    assignments, objective_value = solve_projects(projects, students, choice_matrix, project_caps)
    assert objective_value == 12, 'The objective value is incorrect.'
    assert assignments == [[0, 0, 1], [0, 1, 0], [1, 0, 0], [0, 0, 1]], 'The assignments are incorrect.'

    # Test 2
    students = 3
    projects = 3
    choice_matrix = [[2, 1, 3], [1, 3, 2], [3, 2, 1]]
    project_caps = [2, 2, 2]
    assignments, objective_value = solve_projects(projects, students, choice_matrix, project_caps)
    assert objective_value == 9, 'The objective value is incorrect.'
    assert assignments == [[0, 0, 1], [0, 1, 0], [1, 0, 0]], 'The assignments are incorrect.'

    # Test 3
    students = 4
    projects = 3
    choice_matrix = [[2, 1, 3], [1, 3, 2], [3, 2, 1], [1, 2, 3]]
    project_caps = [1, 1, 1]
    try:
        assignments, objective_value = solve_projects(projects, students, choice_matrix, project_caps)
    except AssertionError:
        pass
    else:
        raise AssertionError('The problem should not have an optimal solution.')


test_solve_projects()
