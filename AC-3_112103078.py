from collections import deque


class CSP:
    def __init__(self, variables, domains, constraints):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints


def ac3(csp):
    queue = deque()

    # Initialize the queue with all the arcs in the CSP
    for Xi in csp.variables:
        for Xj in csp.variables:
            if Xi != Xj:
                queue.append((Xi, Xj))

    while queue:
        Xi, Xj = queue.popleft()

        if revise(csp, Xi, Xj):
            if len(csp.domains[Xi]) == 0:
                return False

            for Xk in get_neighbors_except_Xj(Xi, csp):
                queue.append((Xk, Xi))

    return True


def revise(csp, Xi, Xj):
    revised = False

    for x in csp.domains[Xi][:]:  # Make a copy of the domain to iterate over
        if not any(is_valid_assignment(x, y, Xi, Xj, csp) for y in csp.domains[Xj]):
            csp.domains[Xi].remove(x)
            revised = True

    return revised


def is_valid_assignment(color1, color2, Xi, Xj, csp):
    for constraint in csp.constraints:
        if {Xi, Xj} == set(constraint):
            return color1 != color2

    # If constraint not found, assume it is satisfied
    return True


def get_neighbors_except_Xj(Xi, csp):
    neighbors = []
    for Xk in csp.variables:
        if Xk != Xi:
            neighbors.append(Xk)
    return neighbors


# Define your CSP with variables, domains, and constraints
variables = ["Estonia", "Russia", "Latvia", "Lithuania", "Belarus", "Kaliningrad", "Poland"]
domains = {
    "Estonia": ["Green", "Blue", "Red"],
    "Russia": ["Red"],  # Initialize Russia's domain with "Red"
    "Latvia": ["Green", "Blue", "Red"],
    "Lithuania": ["Green", "Blue", "Red"],
    "Belarus": ["Green", "Blue", "Red"],
    "Kaliningrad": ["Green", "Blue", "Red"],
    "Poland": ["Green", "Blue", "Red"]
}
# Ensure that the constraints enforce different colors for adjacent cities
constraints = [
    ["Estonia", "Russia"],
    ["Estonia", "Latvia"],
    ["Russia", "Latvia"],
    ["Russia", "Belarus"],
    ["Latvia", "Lithuania"],
    ["Latvia", "Belarus"],
    ["Belarus", "Lithuania"],
    ["Belarus", "Poland"],
    ["Kaliningrad", "Lithuania"],
    ["Kaliningrad", "Poland"],
    ["Lithuania", "Poland"],
]

csp = CSP(variables, domains, constraints)

result = ac3(csp)

if result:
    print("Consistency is maintained. Neighboring cities have different colors:")

    for variable in csp.variables:
        print(f"{variable}: {', '.join(csp.domains[variable])}")
else:
    print("Inconsistency found. Constraint violation detected.")
