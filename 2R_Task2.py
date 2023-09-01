import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

L1 = 1.0  
L2 = 1.0 
m1 = 1
m2 = 1

def curve(t):
    x = 1
    y = 1
    return x, y

def inverse_kinematics(x, y):
    c2 = (x**2 + y**2 - L1**2 - L2**2) / (2 * L1 * L2)
    s2 = np.sqrt(1 - c2**2)
    q2 = np.arctan2(s2, c2)
    q1 = np.arctan2(y, x) - np.arctan2(L2 * s2, L1 + L2 * c2)
    return q1, q2

timesteps = 1000
t_vals = np.linspace(0, 2 * np.pi, timesteps)

fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
x3, y3 = 2.26472, 0
x4, y4 = 0, 2.26472


# Plot the line segment
ax.plot([x3, x4], [y3, y4], marker='o')


link1, = ax.plot([], [], 'b-', lw=2)
link2, = ax.plot([], [], 'r-', lw=2)
endpoint, = ax.plot([], [], 'bo')


def fun_animation(frame):
    t = t_vals[frame]
    x_d, y_d = curve(t)
    q1, q2 = inverse_kinematics(x_d, y_d)

    Nx = 10
    Ny = 10

    tau1 = Ny*L1*np.cos(q1) - Nx*L1*np.sin(q1)
    tau2 = Ny*L2*np.cos(q2) - Nx*L2*np.sin(q2)

   

    alpha1 = tau1 / (1/12 *m1 * L1**2 + m2 * (L1**2 + L2**2))
    alpha2 = tau2 / (1/3*m2 * L2**2)
    
    omega1,omega2=0,0
    omega1 += alpha1 * 0.01
    omega2 += alpha2 * 0.01
    q1 += omega1 
    q2 += omega2 

    x1 = L1 * np.cos(q1)
    y1 = L1 * np.sin(q1)
    x2 = x1 + L2 * np.cos(q1 + q2)
    y2 = y1 + L2 * np.sin(q1 + q2)
    
    link1.set_data([0, x1], [0, y1])
    link2.set_data([x1, x2], [y1, y2])
    endpoint.set_data(x2, y2)
    

    return link1, link2, endpoint   

ani = FuncAnimation(fig, fun_animation, frames=timesteps, blit=True)
plt.show()
