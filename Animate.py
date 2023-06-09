# Visualize the movement by animation

import matplotlib.pyplot as plt
from matplotlib import animation

def Animation(points,simulation,figure_center=(0,0),figure_size=1e5,duration=10.0,fps=50,speed=1.0,name='Animation.gif'):
  fig = plt.figure()
  ax = plt.axes(xlim=(-figure_size+figure_center[0], figure_size+figure_center[0]), ylim=(-figure_size+figure_center[1], figure_size+figure_center[1]))
  ax.set_aspect('equal')
  plots = [ax.plot([], [], 'o')[0] for i in points]

  # animation function.  This is called sequentially
  step = round(10*speed)
  def animate(i):
    simulation(points,dt=0.01,steps=step)
    for i,point in enumerate(points):
      plots[i].set_data(point.coordinate[0],point.coordinate[1])
    return tuple(plots)

  # call the animator.  blit=True means only re-draw the parts that have changed.
  anim = animation.FuncAnimation(fig, animate, frames = round(fps*duration), interval = 1000 / fps)

  plt.show()
  
  # save animation as GIF
  anim.save(name)
