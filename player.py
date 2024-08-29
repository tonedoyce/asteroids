# import circleshape class, screen and player attributes
from circleshape import *
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.position = pygame.Vector2(x,y)
        self.rotation = 0

    def triangle(self):
        # will look like triangle but have circle hitbox
        # draws the triangle:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, surface):
        # overrides circleshape.draw()
        pygame.draw.polygon(surface, "white", self.triangle(), 2)

    def rotate(self, dt):
        # rotates the player
        self.rotation += dt * PLAYER_TURN_SPEED

    def move(self, dt):
        # moves the player
        self.position += pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SPEED * dt

    
    def update(self, dt):
        # call movement fcts on key prss
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt * -1)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)