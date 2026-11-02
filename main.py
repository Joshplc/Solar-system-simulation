import math
import pygame
from physics import calculate_gravitational_force, update_position


pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
WIDTH, HEIGHT = screen.get_size()
pygame.display.set_caption("Sonne, Planet & Mond Simulation")
clock = pygame.time.Clock()

#Colors
BG_COLOR = (15, 15, 25)
SUN_COLOR = (255, 204, 0)
PLANET_COLOR = (51, 153, 255)
MOON_COLOR = (200, 200, 200)

#Screen's center as simulation's center
cx, cy = WIDTH / 2, HEIGHT / 2

# Objects
sun = {"x": cx, "y": cy, "mass": 8000, "radius": 30}

planet = {
    "x": cx,
    "y": cy - 500,
    "vx": 3.5,
    "vy": 0.0,
    "mass": 20,
    "radius": 5,
}

moon = {
    "x": cx,
    "y": cy - 475,  # Start close over the planet
    "vx": 4,  # Look at the proportion between Earth and Moon velocity
    "vy": 0.0,
    "mass": 2,
    "radius": 2,
}

G = 1.0
DT = 1  # Makes the simulation slower

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT or (
        event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
    ):
      running = False

  #Calculations, should I include this in another file? Probably

  # Sun attracting planet
  ax_p, ay_p, _ = calculate_gravitational_force(sun, planet, G)
  update_position(planet, ax_p, ay_p, DT)

  #Moon interacts with both Sun and Planet, planet only with sun, and sun with noone
  # I can make everyone interact with everyone, but the distances are not real at all, so wouldn't work with a first appx
  #This approx is leider not working, real orbits are in a quasi unstable equilibrium, if the parameters are not correct, the 
  #equilibrium will be broken.
  ax_mp, ay_mp, _ = calculate_gravitational_force(planet, moon, G)
  ax_ms, ay_ms, _ = calculate_gravitational_force(sun, moon, G)
  ax_mt, ay_mt = ax_mp + ax_ms, ay_mp + ay_ms

  update_position(moon, ax_mt, ay_mt, DT)



  # Show the background
  screen.fill(BG_COLOR)

  # Show the planet, sun and moon
  pygame.draw.circle(
      screen, SUN_COLOR, (int(sun["x"]), int(sun["y"])), sun["radius"]
  )
  pygame.draw.circle(
      screen,
      PLANET_COLOR,
      (int(planet["x"]), int(planet["y"])),
      planet["radius"],
  )
  pygame.draw.circle(
      screen, MOON_COLOR, (int(moon["x"]), int(moon["y"])), moon["radius"]
  )

  pygame.display.flip()
  clock.tick(60)

pygame.quit()