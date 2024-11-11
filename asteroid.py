import pygame
import random
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
        
    def draw(self, screen):
        # pygame.draw.circle(surface, color, center, radius, width)
        pygame.draw.circle(screen, (255,255,255), (self.position.x, self.position.y), self.radius, width=2)

    def update(self, dt):
       self.position += self.velocity * dt

    #split method for when a player shot collides with an asteroid. If the asteroid
    #is the smallest size it simply despawns the object. otherwise it despawns that asteroid
    #spawns in 2 more in the next lower size and gives a randon trajectory angle
    #also adds to the relavent groups so main.py recognizes the newly spawned asteroids as such
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        spawnAngle = random.uniform(20, 50)
        Roid1 = self.velocity.rotate(spawnAngle)
        Roid2 = self.velocity.rotate(-spawnAngle)

        spawnedRoid1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        spawnedRoid2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)

        spawnedRoid1.velocity = Roid1 * 1.2
        spawnedRoid2.velocity = Roid2 * 1.2

        for group in self.groups():
            group.add(spawnedRoid1, spawnedRoid2)