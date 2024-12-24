import pygame
from constants import *
from player import *
from circleshape import *
from asteroid import *
from asteroidfield import *

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteriods = pygame.sprite.Group()
shots = pygame.sprite.Group()

Player.containers = (updatable, drawable)
Asteroid.containers = (updatable, drawable, asteriods)
AsteroidField.containers = (updatable)
Shot.containers = (updatable, drawable, shots)



def main():

    pygame.init()

    print ("Starting asteroids!")
    print (f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    field = AsteroidField()

    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill(color = "black")

        for dr in drawable:
            dr.draw(screen)
        for upd in updatable:
            upd.update(dt)
        
        pygame.display.flip()

        for ast in asteriods:
            if ast.collision(player) == True:
                print ("Game over!")
                return
        
        for asti in asteriods:
            for bully in shots:
                if asti.collision(bully) == True:
                    asti.split()
                    bully.kill()

        dt = clock.tick(60) / 1000
    

if __name__ == "__main__":
    main()