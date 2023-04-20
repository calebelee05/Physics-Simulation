import numpy as np
from PointMass import Point
from Animate import Animation

# Define each points (Mass, (x,y))
Sun = Point(0.5e20,(0.0,0.0))
Mercury = Point(1.0e7,(-10000.0,0.0))
Venus = Point(5.0e16,(0.0,-20000.0))
Earth = Point(6.0e16,(0.0,50000.0))
Moon = Point(7.0e11,(1500.0,50000.0))
Mars = Point(6.0e15,(80000.0,0.0))

# Set initial velocity
Sun.velocity = np.array([0.0,0.0])
Mercury.velocity = np.array([0.0,600.0])
Venus.velocity = np.array([-400.0,0.0])
Earth.velocity = np.array([250.0,0.0])
Moon.velocity = np.array([250.0,60.0])
Mars.velocity = np.array([0.0,-200.0])

# Set initial acceleration
Sun.acceleration = np.array([0.0,0.0])
Mercury.acceleration = np.array([0.0,0.0])
Venus.acceleration = np.array([0.0,0.0])
Earth.acceleration = np.array([0.0,0.0])
Moon.acceleration = np.array([0.0,0.0])
Mars.acceleration = np.array([0.0,0.0])

# List of points to simulate
points = [Sun,Mercury,Venus,Earth,Moon,Mars]

# Animate the simulation

Animation(points,name="Solar_System.gif")
