class CSP:
    def __init__(self, variables, domains, constraints):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints

    def get_neighbors(self, variable):
        neighbors = []
        for constraint in self.constraints:
            if variable in constraint:
                for neighbor in constraint:
                    if neighbor != variable:
                        neighbors.append(neighbor)
        return neighbors


def is_complete(assignment, csp):
    return set(assignment.keys()) == set(csp.variables)


def select_unassigned_variable(csp):
    for variable in csp.variables:
        if variable not in assignment:
            return variable
    return None


def order_domain_values(var, assignment, csp):
    return csp.domains[var]


def is_consistent(value, var, assignment, csp):
    neighbors = csp.get_neighbors(var)
    for neighbor in neighbors:
        if neighbor in assignment and assignment[neighbor] == value:
            return False
    return True


def inference(csp, var, value):
    return {}


def backtrack(assignment, csp):
    if is_complete(assignment, csp):
        # Print the current assignment
        print("Solution found:", assignment)
        return

    var = select_unassigned_variable(csp)
    for value in order_domain_values(var, assignment, csp):
        if is_consistent(value, var, assignment, csp):
            assignment[var] = value
            inferences = inference(csp, var, value)
            if inferences is not None:
                assignment.update(inferences)
                backtrack(assignment, csp)
                for key in inferences:
                    del assignment[key]
            del assignment[var]


variables = ["Estonia", "Russia", "Lativa", "Lithuania", "Belarus", "Kaliningrad", "Poland"]

domains = {
    "Estonia": ["Red", "Green", "Blue"],
    "Russia": ["Red", "Green", "Blue"],
    "Lativa": ["Red", "Green", "Blue"],
    "Lithuania": ["Red", "Green", "Blue"],
    "Belarus": ["Red", "Green", "Blue"],
    "Kaliningrad": ["Red", "Green", "Blue"],
    "Poland": ["Red", "Green", "Blue"]
}

constraints = [
    ["Estonia", "Russia"],
    ["Estonia", "Lativa"],
    ["Russia", "Lativa"],
    ["Russia", "Belarus"],
    ["Lativa", "Lithuania"],
    ["Lativa", "Belarus"],
    ["Belarus", "Lithuania"],
    ["Belarus", "Poland"],
    ["Kaliningrad", "Lithuania"],
    ["Kaliningrad", "Poland"],
    ["Lithuania", "Poland"],
]

csp = CSP(variables, domains, constraints)

assignment = {}

solution = backtrack(assignment, csp)

if solution is not None:
    print("Solution found:", solution)
else:
    print("No solution found.")
#
# import tkinter as tk
#
# class CSPGUI:
#     def __init__(self, root, csp):
#         self.root = root
#         self.csp = csp
#         self.assignment = {}
#
#         self.colors = {
#             "Red": "red",
#             "Green": "green",
#             "Blue": "blue",
#         }
#
#         self.create_gui()
#         self.backtrack()
#
#     def create_gui(self):
#         self.frame = tk.Frame(self.root)
#         self.frame.pack()
#
#         for variable in self.csp.variables:
#             label = tk.Label(self.frame, text=variable)
#             label.grid(row=self.csp.variables.index(variable), column=0)
#             self.assignment[variable] = tk.StringVar()
#             self.assignment[variable].set("Choose Color")
#             options = tk.OptionMenu(self.frame, self.assignment[variable], *self.colors.keys())
#             options.grid(row=self.csp.variables.index(variable), column=1)
#
#         solve_button = tk.Button(self.frame, text="Solve", command=self.backtrack)
#         solve_button.grid(row=len(self.csp.variables), column=0, columnspan=2)
#
#     def is_complete(self):
#         return all(self.assignment.values())
#
#     def is_consistent(self, var, value):
#         neighbors = self.csp.get_neighbors(var)
#         for neighbor in neighbors:
#             neighbor_color = self.assignment.get(neighbor)
#             if neighbor_color == value:
#                 return False
#         return True
#
#     def backtrack(self):
#         if self.is_complete():
#             self.show_solution()
#             return
#
#         var = self.select_unassigned_variable()
#         for value in self.csp.domains[var]:
#             if self.is_consistent(var, value):
#                 self.assignment[var].set(value)
#                 self.root.update()
#                 self.root.after(100)  # Add a delay to visualize the solving process
#                 self.backtrack()
#                 self.assignment[var].set("Choose Color")
#
#     def select_unassigned_variable(self):
#         for variable in self.csp.variables:
#             if not self.assignment[variable].get() == "Choose Color":
#                 continue
#             return variable
#
#     def show_solution(self):
#         solution_window = tk.Toplevel(self.root)
#         solution_window.title("Solution")
#         for variable, color_var in self.assignment.items():
#             color = color_var.get()
#             if color == 'Choose Color':
#                 color = 'Red'  # Set the color to 'White' for unassigned variables
#             if color not in self.colors:
#                 color = 'Red'  # Set a default color for any unexpected color values
#             label = tk.Label(solution_window, text=f"{variable}: {color_var.get()}", bg=self.colors[color])
#             label.pack()
#
#
# class CSP:
#     def __init__(self, variables, domains, constraints):
#         self.variables = variables
#         self.domains = domains
#         self.constraints = constraints
#
#     def get_neighbors(self, variable):
#         neighbors = []
#         for constraint in self.constraints:
#             if variable in constraint:
#                 for neighbor in constraint:
#                     if neighbor != variable:
#                         neighbors.append(neighbor)
#         return neighbors
#
# if __name__ == "__main__":
#     root = tk.Tk()
#     root.title("CSP Color Assignment")
#
#     variables = ["Estonia", "Russia", "Lativa", "Lithuania", "Belarus", "Kaliningrad", "Poland"]
#
#     domains = {
#         "Estonia": ["Red", "Green", "Blue"],
#         "Russia": ["Red", "Green", "Blue"],
#         "Lativa": ["Red", "Green", "Blue"],
#         "Lithuania": ["Red", "Green", "Blue"],
#         "Belarus": ["Red", "Green", "Blue"],
#         "Kaliningrad": ["Red", "Green", "Blue"],
#         "Poland": ["Red", "Green", "Blue"]
#     }
#
#     constraints = [
#         ["Estonia", "Russia"],
#         ["Estonia", "Lativa"],
#         ["Russia", "Lativa"],
#         ["Russia", "Belarus"],
#         ["Lativa", "Lithuania"],
#         ["Lativa", "Belarus"],
#         ["Belarus", "Lithuania"],
#         ["Belarus", "Poland"],
#         ["Kaliningrad", "Lithuania"],
#         ["Kaliningrad", "Poland"],
#         ["Lithuania", "Poland"],
#     ]
#     csp = CSP(variables, domains, constraints)
#     app = CSPGUI(root, csp)
#     root.mainloop()
