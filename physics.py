import math


def update_position(obj, ax, ay, dt):
  """Actualize velocity and position depending on time steps"""
  obj["vx"] += ax * dt
  obj["vy"] += ay * dt
  obj["x"] += obj["vx"] * dt
  obj["y"] += obj["vy"] * dt


def calculate_gravitational_force(obj1, obj2, G):
  """Calculates the gravitational attraction of two bodies"""
  dx = obj1["x"] - obj2["x"]
  dy = obj1["y"] - obj2["y"]
  distance = math.hypot(dx, dy)

  if distance < 5:  # Avoids division by zero
    return 0, 0, distance

  force = (G * obj1["mass"]) / (distance**2)
  ax = force * (dx / distance)
  ay = force * (dy / distance)
  return ax, ay, distance