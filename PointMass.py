import numpy as np

G = 6.6743e-11

class Point:
  def __init__(self, mass, coordinate, dim=2):
    self.dim = dim
    self.mass = mass                                        # scalar mass
    self.coordinate = np.array(coordinate)                  # vector coordinate
    self.velocity = np.array([0.0 for n in range(dim)])     # vector velocity
    self.acceleration = np.array([0.0 for n in range(dim)]) # vector acceleration
    self.dt = 0.1                                           # time step for updating velocity and displacement
  
  # Calculate the displacement vector from current position with object 2
  def Displacement(self, other):
    Coordinate1 = self.coordinate
    Coordinate2 = other.coordinate
    displacement = Coordinate2-Coordinate1
    return displacement
  
  # Calculate distance from object 2
  def Distance(self, other):
    displacement = self.Displacement(other)
    r = np.linalg.norm(displacement)
    return r
  
  # Calculate the graviational force
  def Force(self, other):
    r = self.Distance(other)
    M = other.mass
    _F_ = G * self.mass * M / r**2
    displacement = self.Displacement(other)
    direction = displacement / r
    F = direction * _F_
    return F
  
  # Add up the forces to get the net force
  def NetForce(self, others):
    F = np.array([0.0 for n in range(self.dim)])
    for other in others:
      F += self.Force(other)
    return F
  
  # Update acceleration, velocity, and position of point
  def update(self, F, dt):
    self.acceleration = F / self.mass
    self.velocity += self.acceleration * dt
    self.coordinate += self.velocity * dt
