# import circleshape class
from circleshape import CircleShape

#import pygame
import pygame

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