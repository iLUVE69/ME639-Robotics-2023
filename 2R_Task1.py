import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Arm lengths
L1 = 1.0
L2 = 1.0

num_steps = 100
theta1_range = np.linspace(0, np.pi, num_steps)
theta2_range = np.linspace(0, np.pi, num_steps)

fig, ax = plt.subplots()
line, = ax.plot([], [], 'o-', lw=2)
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('2R Robotic Arm Simulation')

# Initialization function for animation
def init():
    line.set_data([], [])
    return line,

def animate(i):
    theta1 = theta1_range[i]
    theta2 = theta2_range[i]
    x = [0, L1 * np.cos(theta1), L1 * np.cos(theta1) + L2 * np.cos(theta1 + theta2)]
    y = [0, L1 * np.sin(theta1), L1 * np.sin(theta1) + L2 * np.sin(theta1 + theta2)]
    line.set_data(x, y)
    return line,

ani = FuncAnimation(fig, animate, frames=num_steps, init_func=init, blit=True)

plt.show()
