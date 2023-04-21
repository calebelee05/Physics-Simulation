import numpy as np

G = 6.6743e-11
k = 8.9876e9

class Point:
  def __init__(self, coordinate, mass=1.0, charge=0.0, dim=2, fixed=False):
    self.dim = dim                                                          # N-dimensions
    self.mass = mass                                                        # scalar mass
    self.coulomb = charge * 1.602e-19                                       # scalar charge in coulombs
    self.coordinate = np.array(coordinate).astype(float)                    # coordinate vector
    self.velocity = np.array([0.0 for n in range(dim)]).astype(float)       # velocity vector
    self.ConstantForce = np.array([0.0 for n in range(dim)]).astype(float)  # constant force vector
    self.netforce = self.ConstantForce                                      # Net force vector
    self.dt = 0.1                                                           # timestep for updating velocity and displacement
    self.fixed = fixed                                                      # whether the point is fixed in place
  
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
  def GravitationalForce(self, other):
    r = self.Distance(other)
    M = other.mass
    _F_ = G * self.mass * M / r**2
    displacement = self.Displacement(other)
    direction = displacement / r
    F = direction * _F_
    return F
  
  # Calculate the electrostatic force
  def ElectrostaticForce(self,other):
    r = self.Distance(other)
    Q = other.coulomb
    _F_ = -k * self.coulomb * Q / r**2
    displacement = self.Displacement(other)
    direction = displacement / r
    F = direction * _F_
    return F
  
  # Calculate the total net force
  def NetForce(self, others=None):
    if others:
      for other in others:
        self.netforce += self.GravitationalForce(other) + self.ElectrostaticForce(other)

  # Update the position and velocity
  def update(self, others=None, dt=0.1):
    if self.fixed:
      return
    self.NetForce(others)
    self.acceleration = self.netforce / self.mass
    self.velocity += self.acceleration * dt
    self.coordinate += self.velocity * dt
