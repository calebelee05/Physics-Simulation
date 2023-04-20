# Visualize the movement by animation

import matplotlib.pyplot as plt
from matplotlib import animation
from Simulate import simulate

def Animation(points,frames,interval,save_gif=True,name='Animation.gif'):
  fig = plt.figure()
  ax = plt.axes(xlim=(-1e5, 1e5), ylim=(-1e5, 1e5))
  ax.set_aspect('equal')
  plots = [ax.plot([], [], 'o')[0] for i in points]


  # animation function.  This is called sequentially
  def animate(i):
    simulate(points,steps=10)
    for i,point in enumerate(points):
      plots[i].set_data(point.coordinate[0],point.coordinate[1])
    return tuple(plots)

  # call the animator.  blit=True means only re-draw the parts that have changed.
  anim = animation.FuncAnimation(fig, animate, frames=frames, interval=interval)

  plt.show()
  
  # Save animation as GIF
  if save_gif:
    anim.save(name)
