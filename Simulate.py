# Simulate the movement of the set of points
# timestep of (dt) seconds, updated (steps) times
def simulate(points, dt=0.1, steps=1000):
  n = len(points)
  Coordinates = [[] for j in range(n)]
  for _ in range(steps):
    for i, point in enumerate(points):
      OtherPoints = points.copy()
      del OtherPoints[i]
      point.update(OtherPoints, dt)
      Coordinates[i].append(point.coordinate)
  
  # Return the history of the position of each points
  return Coordinates
