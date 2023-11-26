from pulp import LpMaximize, LpProblem, LpVariable, LpStatus, PULP_CBC_CMD

# Define the problem
problem = LpProblem("Maximize_Profit", LpMaximize)

# Define the variables
x_A = LpVariable('x_A', lowBound=0, cat='Integer')  # Product A
x_B = LpVariable('x_B', lowBound=0, cat='Integer')  # Product B
# x_A = LpVariable('x_A', lowBound=0)  # Product A
# x_B = LpVariable('x_B', lowBound=0)  # Product B
y = LpVariable('y', lowBound=0)  # Continuous variable for Resource R2

# Objective function
problem += 15 * x_A + 25 * x_B - 10 * y, "Total Profit"

# Constraints
problem += 3 * x_A + 3.5 * x_B - 10 * y <= 60, "Resource R1 Constraint"
problem += 2 * x_A + 3 * x_B + y == 70, "Resource R2 Constraint"
problem += x_A + x_B >= 30, "Min products constraint"
problem += x_A >= 1, "Min product 1 constraint"
problem += x_A <= 25, "Max product 1 constraint"
problem += x_B >= 5, "Min product 2 constraint"
problem += y >= 1, "Min additional resource constraint"

# Solve the problem
problem.solve()

# Output the results
solution = {
    "Product A": x_A.varValue,
    "Product B": x_B.varValue,
    "Additional Resource R2": y.varValue,
    "Total Profit": problem.objective.value()
}

print(solution)
