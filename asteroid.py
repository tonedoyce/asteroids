# import circleshape class
from circleshape import CircleShape

#import pygame
import pygame

from constants import *
import random

class Asteroid(CircleShape):
    containers = None

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, surface):
        # overrides circleshape.draw
        pygame.draw.circle(surface, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        # overrides circleshape.update
        self.position += self.velocity * dt

    def split(self):
        # splits on hit by shoot
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return None
        else:
            phirand = random.uniform(20,50)
            self.velocity = self.velocity.rotate(-phirand) * 1.2
            v_1 = self.velocity.rotate(phirand) * 1.2
            v_2 = self.velocity.rotate(-phirand) * 1.2
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_1.velocity = v_1
            asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_2.velocity = v_2
            asteroid_1.containers = self.containers
            asteroid_2.containers = self.containers
            self.kill()