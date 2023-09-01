import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Arm lengths
L1 = 1.0
L2 = 1.0

num_steps = 50
theta1_range = np.linspace(0.610865,  2.53073, num_steps) # 0.610865 = 35 degrees
theta2_range = np.linspace(0.610865, 2.53073, num_steps)   # 2.53073 = 145 degrees

fig, ax = plt.subplots()
line, = ax.plot([], [], 'o-', lw=2)
path_line, = ax.plot([], [], 'r--', lw=1)  
theta_text = ax.text(0.02, 0.95, '', transform=ax.transAxes)  
ax.set_ylim(-2, 2)
ax.set_xlim(-2, 2)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('2R Robotic Arm Simulation')

# Initialization function for animation
def init():
    line.set_data([], [])
    path_line.set_data([], [])  
    theta_text.set_text('')
    return line, path_line, theta_text

path_points = []  

def animate(i):
    global path_points
    
    theta1 = theta1_range[i]
    theta2 = theta2_range[i]
    x = [0, L1 * np.cos(theta1), L1 * np.cos(theta1) + L2 * np.cos(theta1 + theta2)]
    y = [0, L1 * np.sin(theta1), L1 * np.sin(theta1) + L2 * np.sin(theta1 + theta2)]
    
    path_points.append([x[-1], y[-1]]) 
    path_line.set_data(*zip(*path_points))  
    
    line.set_data(x, y)
    
    theta_text.set_text(f'Theta1: {theta1:.2f}\nTheta2: {theta2:.2f}')  
    
    return line, path_line, theta_text

ani = FuncAnimation(fig, animate, frames=num_steps, init_func=init, blit=True)

plt.show()
