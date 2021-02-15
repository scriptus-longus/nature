import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation
from systems import DoublePendulum as two_pend

#theta1 = random.uniform(-2*np.pi, 2*np.pi)
#theta2 = random.uniform(-2*np.pi, 2*np.pi)
save_ani = False

pend = two_pend(1,1,1,1,9.81, "random")
pend.trajectory([pend.theta1, 0, pend.theta2, 0], np.linspace(0,30,700))

fig,ax = plt.subplots()

ax.set_facecolor("#293437")
trail_r_x, trail_r_y = [], []
trail_b_x, trail_b_y = [], []



line1, = plt.plot([], [], "o", color="#2A444B")
line2, = plt.plot([], [], "ro")
line3, = plt.plot([], [], color="#2A444B", linestyle="-", linewidth=1)
line4, = plt.plot([], [], color="#F7E226", linestyle="-", linewidth=1)


def init():
    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)
    line1.set_data([], [])
    line2.set_data([], [])
    line3.set_data([], [])
    line4.set_data([], [])
    return line3, line4, line1, line2


def animate(frame):
    x1_plot,y1_plot = pend.x1[frame],pend.y1[frame]
    x2_plot,y2_plot = pend.x2[frame], pend.y2[frame]
    
    trail_b_x.append(x1_plot)
    trail_b_y.append(y1_plot)
    
    trail_r_x.append(x2_plot)
    trail_r_y.append(y2_plot)
    
    
    line1.set_data(x1_plot, y1_plot)
    line2.set_data(x2_plot, y2_plot)
    
    line3.set_data(trail_b_x, trail_b_y)
    line4.set_data(trail_r_x, trail_r_y)
    #line3.set_data([x1_plot, x2_plot], [y1_plot, y2_plot])
    #line4.set_data([x1_plot, 0], [y1_plot, 0])
    return line1, line2, line3, line4


ani = FuncAnimation(fig, animate, frames=700,
                    init_func=init, interval=30, blit=True)
if save_ani:
  Writer = animation.writers["ffmpeg"]
  writer = Writer(fps=23, metadata=dict(artist="scriptus_longus"), bitrate=1800)

  ani.save("double_pend.mp4", writer=writer)

plt.show()
