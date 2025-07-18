# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroidfield import *
from asteroid import *
import sys
from shot import *

def main():

    #Setup
    pygame.init

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    player1.shots_group = shots
    asteroidfield1 = AsteroidField()

    #Program starts:
    print("Starting Asteroids!")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        shots.update(dt)
        for item in drawable:
            item.draw(screen)
        for item in asteroids:
            if item.collision_detection(player1):
                print("Game over!")
                sys.exit()
        for item in asteroids:
            for shot_fired in shots:
                if item.collision_detection(shot_fired):
                    item.split()
                    shot_fired.kill()

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()