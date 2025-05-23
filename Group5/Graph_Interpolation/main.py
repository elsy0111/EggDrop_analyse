import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline

# Original Data
x = [0, 0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4, 1.6, 1.8, 2, 2.2, 2.4]
y = [10, 9.80916, 9.19847, 8.16794, 6.87023, 5.572519, 4.35115, 3.28244, 2.32824, 1.48855, 0.725191, 0.152672, 0]

# Interpolation function
cs = CubicSpline(x, y)

# New x values at 0.1 intervals
x_new = np.arange(0, 2.4, 0.0199)
y_new = cs(x_new)

# First derivative
dy_dx = -cs.derivative()(x_new)

# Second derivative
d2y_dx2 = -cs.derivative(2)(x_new)

# Plot the original data
plt.figure(figsize=(10, 6))

# Original data
plt.plot(x, y, 'o', label='height from ground', color='blue')

# Interpolated data
plt.plot(x_new, y_new, '-', label='Interpolated Data', color='red')

# First derivative
plt.plot(x_new, dy_dx, '--', label='velocity', color='green')

# Second derivative
plt.plot(x_new, d2y_dx2, '-.', label='acceleration', color='purple')

# Set limits for x and y axes
plt.ylim(-12.5, 12.5)
plt.xlim(0, 2.5)

# Labels and title
plt.xlabel('')
plt.ylabel('')
plt.title('')
plt.legend()
plt.grid(True)

# Show plot
# plt.show()
plt.savefig('interpolation_plot.png', dpi=300, bbox_inches='tight')
