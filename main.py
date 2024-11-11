import pygame
from constants import *
from circleshape import CircleShape
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    tickRate = pygame.time.Clock()


    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    asteroidField = AsteroidField()
    Shot.containers = (shots)
    
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    dt = 0

    while True:
        #checks through the event.get() log if the user commits an exit or QUIT command
        #such as clicking the X button to exit the program, then cleanly ends the program run-time
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        

        #Screen is filled using the colour BLACK with the RGB values 0,0,0
        screen.fill((0,0,0))

        #pulls from the player.py file for the update member function of the Player class
        #this checks every frame if the user has pressed the keys 'a' or 'd' to rotate the
        #player model
        for obj in updatable:
            obj.update(dt)
        
        #Player model is drawn to the screen
        for obj in drawable:
            obj.draw(screen)

        #ends the game if the player ship model collides with an asteroid
        for asteroid in asteroids:
            if asteroid.collision(player) == True:
                print("Game over!")
                exit(1)
            #handles collison detection between asteroids and player shots
            for shot in shots:
                if shot.collision(asteroid) == True:
                    shot.kill()
                    asteroid.split()
        
        # Update all shots
        for shot in shots:
            shot.update(dt)

        # Draw all shots
        for shot in shots:
            shot.draw(screen)


        #double buffering function that 'flips' from the front currently displayed buffer frame
        #to the back buffered frame, ensuring minimized screen tearing and flicker during
        #screen refreshes
        pygame.display.flip()

        #dt or Delta Time effectively caps the framerate to 60 FPS using tickRate's 
        # member function .tick(), which is actually part of pygame.time.Clock()
        # .tick() returns in ms (milliseconds) so the divison by 1000 converts to seconds
        dt = tickRate.tick(60) / 1000


if __name__ == "__main__":
    main()