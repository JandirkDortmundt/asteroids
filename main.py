# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from asteroidfield import AsteroidField
from constants import *
from player import *
from circleshape import *
from asteroid import *
from asteroidfield import *
import sys

from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    player = Player(x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color="black")
        dt = clock.tick(60)/1000

        for i in updatable:
            i.update(dt)
        for i in drawable:
            i.draw(screen)
        
        for i in asteroids:
            if i.collision(player):
                sys.exit("Game over!")
        # player.update(dt)
        # player.draw(screen)
        for i in asteroids:
            for j in shots:
                if i.collision(j):
                    i.split()
                    j.kill()

        pygame.display.flip()
if __name__ == "__main__":
    main()

