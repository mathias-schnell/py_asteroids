# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    # print some initialization statements to console
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # start pygame
    pygame.init()

    # the game screen, clock and time delta
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # sprite containers
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # set the containers for each game object
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    # create the player
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS)
    ast_field = AsteroidField()

    # the game loop
    while True:

        # check for anything that would close the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                return
        
        # calculate time delta
        dt = clock.tick(60) / 1000

        # black background
        screen.fill((0,0,0))

        # update all the updatable objects
        for obj in updatable:
            obj.update(dt)

        # draw all the drawable objects
        for obj in drawable:
            obj.draw(screen)
            # check for collision with the player
            if obj != player and obj.collision_check(player):
                print("Game over!")
                pygame.quit()
                sys.exit()
                return

        # refresh the screen
        pygame.display.flip()

if __name__ == "__main__":
    main()