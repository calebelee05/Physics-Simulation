import numpy as np

G = 6.6743e-11

class Point:
  def __init__(self, mass, coordinate, dim=2):
    self.dim = dim                                                          # N-Dimension
    self.mass = mass                                                        # scalar mass
    self.coordinate = np.array(coordinate).astype(float)                    # coordinate vector
    self.velocity = np.array([0.0 for n in range(dim)]).astype(float)       # velocity vector
    self.ConstantForce = np.array([0.0 for n in range(dim)]).astype(float)  # constant force vector
    self.dt = 0.1                                                           # timestep for updating velocity and displacement
  
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
  
  # Calculate the total net force
  def NetForce(self, others=None):
    F = np.array([0.0 for n in range(self.dim)])
    F += self.ConstantForce
    if others:
      for other in others:
        F += self.Force(other)
    return F
  
  # Update the position and velocity
  def update(self, others=None, dt=0.1):
    F = self.NetForce(others)
    self.acceleration = F / self.mass
    self.velocity += self.acceleration * dt
    self.coordinate += self.velocity * dt
