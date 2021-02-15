import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation
import random

from systems import DoublePendulum as two_pend

save_ani = False

pend1 = two_pend(1, 1, 1, 1, 9.81, "random")
pend2 = two_pend(1, 1, 1, 1, 9.81, "random")
pend3 = two_pend(1, 1, 1, 1, 9.81, "random")

pend1.origin = (-4, 0)
pend3.origin = (4, 0)

time = np.linspace(0,30,700)

pend1.trajectory([pend1.theta1, 0, pend1.theta2, 0], time)
pend2.trajectory([pend2.theta1, 0, pend2.theta2, 0], time)
pend3.trajectory([pend3.theta1, 0, pend3.theta2,0 ], time)

fig, ax = plt.subplots()
ax.set_facecolor("#293437")

trail_w1_p1_x, trail_w1_p1_y = [], []
trail_w2_p1_x, trail_w2_p1_y = [], []

trail_w1_p2_x, trail_w1_p2_y = [], []
trail_w2_p2_x, trail_w2_p2_y = [], []

trail_w1_p3_x, trail_w1_p3_y = [], []
trail_w2_p3_x, trail_w2_p3_y = [], []

orig_p1, = plt.plot([], [], "o", color="#000000", markersize=2)
orig_p2, = plt.plot([], [], "o", color="#000000", markersize=2)
orig_p3, = plt.plot([], [], "o", color="#000000", markersize=2)


w1_p1, = plt.plot([], [], "o", color="#2A444B")
w2_p1, = plt.plot([], [], "ro")

w1_p2, = plt.plot([], [], "o", color="#2A444B")
w2_p2, = plt.plot([], [], "ro")

w1_p3, = plt.plot([], [], "o", color="#2A444B")
w2_p3, = plt.plot([], [], "ro")

ln_w1_p1, = plt.plot([], [], color="#2A444B", linestyle="-", linewidth=1)
ln_w2_p1, = plt.plot([], [], color="#F7E226", linestyle="-", linewidth=1)

ln_w1_p2, = plt.plot([], [], color="#2A444B", linestyle="-", linewidth=1)
ln_w2_p2, = plt.plot([], [], color="#F7E226", linestyle="-", linewidth=1)

ln_w1_p3, = plt.plot([], [], color="#2A444B", linestyle="-", linewidth=1)
ln_w2_p3, = plt.plot([], [], color="#F7E226", linestyle="-", linewidth=1)

def init():
    ax.set_xlim(-8, 8)
    ax.set_ylim(-4, 4)

    orig_p1.set_data([pend1.origin[0]], [pend1.origin[1]])
    orig_p2.set_data([pend2.origin[0]], [pend2.origin[1]])
    orig_p3.set_data([pend3.origin[0]], [pend3.origin[1]])

    w1_p1.set_data([], [])
    w2_p1.set_data([], [])
    ln_w1_p1.set_data([], [])
    ln_w2_p1.set_data([], [])
    
    w1_p2.set_data([], [])
    w2_p2.set_data([], [])
    ln_w1_p2.set_data([], [])
    ln_w2_p2.set_data([], [])
    
    w1_p3.set_data([], [])
    w2_p3.set_data([], [])
    ln_w1_p3.set_data([], [])
    ln_w2_p3.set_data([], [])
    return w1_p1, ln_w1_p1, w2_p1, ln_w2_p1,  w1_p2, ln_w1_p2, w2_p2, ln_w2_p2, w1_p3, ln_w1_p3, w2_p3, ln_w2_p3   

def update(frame):
    x1_p1, y1_p1 = pend1.x1[frame], pend1.y1[frame]
    x2_p1, y2_p1 = pend1.x2[frame], pend1.y2[frame]
    
    x1_p2, y1_p2 = pend2.x1[frame], pend2.y1[frame]
    x2_p2, y2_p2 = pend2.x2[frame], pend2.y2[frame]
    
    x1_p3, y1_p3 = pend3.x1[frame], pend3.y1[frame]
    x2_p3, y2_p3 = pend3.x2[frame], pend3.y2[frame]
    
    w1_p1.set_data(x1_p1, y1_p1)
    w2_p1.set_data(x2_p1, y2_p1)
    
    w1_p2.set_data(x1_p2, y1_p2)
    w2_p2.set_data(x2_p2, y2_p2)
    w1_p3.set_data(x1_p3, y1_p3)
    w2_p3.set_data(x2_p3, y2_p3)
    
    trail_w1_p1_x.append(x1_p1)
    trail_w1_p1_y.append(y1_p1)
    
    trail_w2_p1_x.append(x2_p1)
    trail_w2_p1_y.append(y2_p1)
    
    trail_w1_p2_x.append(x1_p2)
    trail_w1_p2_y.append(y1_p2)
    
    trail_w2_p2_x.append(x2_p2)
    trail_w2_p2_y.append(y2_p2)
    
    trail_w1_p3_x.append(x1_p3)
    trail_w1_p3_y.append(y1_p3)
    
    trail_w2_p3_x.append(x2_p3)
    trail_w2_p3_y.append(y2_p3)
    
    ln_w1_p1.set_data(trail_w1_p1_x, trail_w1_p1_y)
    ln_w2_p1.set_data(trail_w2_p1_x, trail_w2_p1_y)
    
    ln_w1_p2.set_data(trail_w1_p2_x, trail_w1_p2_y)
    ln_w2_p2.set_data(trail_w2_p2_x, trail_w2_p2_y)
    
    ln_w1_p3.set_data(trail_w1_p3_x, trail_w1_p3_y)
    ln_w2_p3.set_data(trail_w2_p3_x, trail_w2_p3_y)
      
    return w1_p1, ln_w1_p1, w2_p1, ln_w2_p1,  w1_p2, ln_w1_p2, w2_p2, ln_w2_p2, w1_p3, ln_w1_p3, w2_p3, ln_w2_p3   

ani = FuncAnimation(fig, update, frames=700,
                    init_func=init, interval=30)

if save_ani:
  Writer = animation.writers["ffmpeg"]
  writer = Writer(fps=23, metadata=dict(artist="scriptus_longus"), bitrate=1800)

  ani.save("double_pend.mp4", writer=writer)

plt.show() 
