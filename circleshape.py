import pygame
from player import *
# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), width=2)
        return

    def update(self, dt):
        # sub-classes must override
        pass

    def collision_detection(self, circleshape_obj):
        if self.position.distance_to(circleshape_obj.position) > self.radius + circleshape_obj.radius:
            return False
        return True