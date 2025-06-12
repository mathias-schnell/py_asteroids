import pygame
import random
from constants import *
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            rand_angle = random.uniform(20, 50)
            new_rad = self.radius - ASTEROID_MIN_RADIUS
            
            new_ast1 = Asteroid(self.position.x, self.position.y, new_rad)
            new_ast1.velocity = self.velocity.rotate(rand_angle) * 1.2

            new_ast2 = Asteroid(self.position.x, self.position.y, new_rad)
            new_ast2.velocity = self.velocity.rotate(-rand_angle) * 1.2