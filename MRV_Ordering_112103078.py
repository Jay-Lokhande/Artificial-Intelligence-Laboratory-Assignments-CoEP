# class CSP:
#     def __init__(self, variables, domains, constraints):
#         self.variables = variables
#         self.domains = domains
#         self.constraints = constraints
#
#
# def is_safe(region, color, assignment, csp):
#     for neighbor in csp.constraints[region]:
#         if neighbor in assignment and assignment[neighbor] == color:
#             return False
#     return True
#
#
# def mrv_ordering(variables, assignment, domains, csp):
#     unassigned = [var for var in variables if var not in assignment]
#     return min(unassigned, key=lambda var: len(domains[var]))
#
#
# def backtrack_search(variables, assignment, domains, csp, solutions):
#     if len(assignment) == len(variables):
#         solutions.append(assignment.copy())  # Found a solution
#         return
#
#     var = mrv_ordering(variables, assignment, domains, csp)
#     for color in domains[var]:
#         if is_safe(var, color, assignment, csp):
#             assignment[var] = color
#             backtrack_search(variables, assignment, domains, csp, solutions)
#             del assignment[var]  # Backtrack
#
#
# def print_solutions(solutions):
#     if solutions:
#         print("All Solutions:")
#         for idx, solution in enumerate(solutions, start=1):
#             print(f"Solution {idx}:")
#             for region, color in solution.items():
#                 print(f"{region}: {color}")
#             print()
#     else:
#         print("No solutions found.")
#
#
# assignment = {}
# solutions = []
#
# variables = ["Estonia", "Russia", "Latvia", "Lithuania", "Belarus", "Kaliningrad", "Poland"]
#
# domains = {
#     "Estonia": ["Red", "Green", "Blue"],
#     "Russia": ["Red", "Green", "Blue"],
#     "Latvia": ["Red", "Green", "Blue"],
#     "Lithuania": ["Red", "Green", "Blue"],
#     "Belarus": ["Red", "Green", "Blue"],
#     "Kaliningrad": ["Red", "Green", "Blue"],
#     "Poland": ["Red", "Green", "Blue"]
# }
#
# constraints = {
#     "Estonia": ["Russia", "Latvia"],
#     "Russia": ["Estonia", "Latvia", "Belarus"],
#     "Latvia": ["Estonia", "Russia", "Lithuania", "Belarus"],
#     "Lithuania": ["Latvia", "Belarus", "Poland"],
#     "Belarus": ["Russia", "Latvia", "Lithuania"],
#     "Kaliningrad": ["Lithuania", "Poland"],
#     "Poland": ["Lithuania", "Kaliningrad"]
# }
#
# csp = CSP(variables, domains, constraints)
#
# backtrack_search(csp.variables, assignment, csp.domains, csp, solutions)
#
# print_solutions(solutions)
def is_valid_assignment(variables, assignment, current_variable, color):
    for neighbor in constraints[current_variable]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def mrv(variables, assignment, domains, constraints):
    unassigned_variables = [var for var in variables if var not in assignment]
    return min(unassigned_variables, key=lambda var: len(domains[var]))

def backtracking_mrv(variables, assignment, domains, constraints, unique_solutions):
    if len(assignment) == len(variables):
        solution = tuple(sorted(assignment.items()))
        if solution not in unique_solutions:
            unique_solutions.add(solution)
            yield assignment.copy()  # All variables are assigned, yield solution
    else:
        current_variable = mrv(variables, assignment, domains, constraints)

        for color in domains[current_variable]:
            if is_valid_assignment(variables, assignment, current_variable, color):
                assignment[current_variable] = color
                yield from backtracking_mrv(variables, assignment, domains, constraints, unique_solutions)
                del assignment[current_variable]

if __name__ == "__main__":
    variables = ["Estonia", "Russia", "Latvia", "Lithuania", "Belarus", "Kaliningrad", "Poland"]

    domains = {
        "Estonia": ["Red", "Green", "Blue"],
        "Russia": ["Red", "Green", "Blue"],
        "Latvia": ["Red", "Green", "Blue"],
        "Lithuania": ["Red", "Green", "Blue"],
        "Belarus": ["Red", "Green", "Blue"],
        "Kaliningrad": ["Red", "Green", "Blue"],
        "Poland": ["Red", "Green", "Blue"]
    }

    constraints = {
        "Estonia": ["Russia", "Latvia"],
        "Russia": ["Estonia", "Latvia", "Belarus"],
        "Latvia": ["Estonia", "Russia", "Lithuania", "Belarus"],
        "Lithuania": ["Latvia", "Belarus", "Poland"],
        "Belarus": ["Russia", "Latvia", "Lithuania"],
        "Kaliningrad": ["Lithuania", "Poland"],
        "Poland": ["Lithuania", "Kaliningrad"]
    }

    unique_solutions = set()
    solutions = list(backtracking_mrv(variables, {}, domains, constraints, unique_solutions))

    if solutions:
        print("All solutions:")
        for i, solution in enumerate(solutions, 1):
            print(f"Solution {i}:")
            for variable, color in solution.items():
                print(f"{variable}: {color}")
            print()
    else:
        print("No solution found.")
