import numpy as np
import matplotlib.pyplot as plt

# Create a grid of values for x_A and x_B
x_A = np.linspace(1, 25, 400)  # x_A between 1 and 25
x_B = np.linspace(5, 70, 400)  # x_B between 5 and 70
x_A, x_B = np.meshgrid(x_A, x_B)

# Calculate y for each constraint
y_constraint_1 = (3 * x_A + 3.5 * x_B - 60) / 10  # rearranged constraint 1 for y
y_constraint_2 = 70 - 2 * x_A - 3 * x_B  # rearranged constraint 2 for y

# Create a 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the constraints
ax.plot_surface(x_A, x_B, y_constraint_1, alpha=0.5, rstride=100, cstride=100, color='blue', label='Constraint 1')
ax.plot_surface(x_A, x_B, y_constraint_2, alpha=0.5, rstride=100, cstride=100, color='yellow', label='Constraint 2')

# Labels and title
ax.set_xlabel('x_A')
ax.set_ylabel('x_B')
ax.set_zlabel('y')
ax.set_title('3D plot of constraints for x_A, x_B, and y')

# For the z-axis, show values only above 0
ax.set_zlim(0, 50)

# Draw the point (24, 6, 4) on the plot
ax.scatter(24, 6, 4, color='green', marker='o', s=100, label='(24, 6, 4)')
ax.scatter(23.33, 6.67, 3.33, color='red', marker='o', s=100, label='(23.33, 6.67, 0)')

# Show the plot
plt.show()
