import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Manipulator parameters
L1 = 1.0  # Length of the first link
L2 = 1.0  # Length of the second link
m1 = 1
m2 = 1

#Path equation
def desired_curve(t):
    x = 1
    y = 1
    return x, y

def inverse_kinematics(x, y):
    c2 = (x**2 + y**2 - L1**2 - L2**2) / (2 * L1 * L2)
    s2 = np.sqrt(1 - c2**2)
    q2 = np.arctan2(s2, c2)
    q1 = np.arctan2(y, x) - np.arctan2(L2 * s2, L1 + L2 * c2)
    return q1, q2

def forward_kinematics(x,y):
    q1,q2 = inverse_kinematics(x,y)
    x1 = L1 * np.cos(q1)
    y1 = L1 * np.sin(q1)
    x2 = x1 + L2 * np.cos(q1 + q2)
    y2 = y1 + L2 * np.sin(q1 + q2)
    return x2,y2

timesteps = 100
t_vals = np.linspace(0, 2 * np.pi, timesteps)

#Animation
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

link1, = ax.plot([], [], 'r-', lw=2)
link2, = ax.plot([], [], 'b-', lw=2)
endpoint, = ax.plot([], [], 'ro')

x0,y0= 1.3,1.3

def fun_animation(frame):
    t = t_vals[frame]
    x_d, y_d = desired_curve(t)
    
    x_current,y_current = x_d,y_d
    delx = x_current - x0
    dely = y_current - y0
    q1, q2 = inverse_kinematics(x_d, y_d)

    kx = 100
    ky = 100

    spring_force_x = -kx*delx
    spring_force_y = -ky*dely

    Nx = -spring_force_x
    Ny = -spring_force_y

    tau1 = Ny*L1*np.cos(q1) - Nx*L1*np.sin(q1)
    tau2 = Ny*L2*np.cos(q2) - Nx*L2*np.sin(q2)


    alpha1 = tau1 / (m1 * L1**2 + m2 * (L1**2 + L2**2))
    alpha2 = tau2 / (m2 * L2**2)
    
    # Angular velocities and angles using Euler's method
    omega1,omega2=0,0
    omega1 += alpha1 * 0.1
    omega2 += alpha2 * 0.1
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
