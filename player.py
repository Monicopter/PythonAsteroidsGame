import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.cooldownTimer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, (255,255,255), self.triangle(), width=2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, direction, dt):
        ## if direction == 1, ship moves forward, if direction == -1 ship will move backwards
        forward = pygame.Vector2(0, direction).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    


    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.move(1, dt)

        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.move(-1, dt)

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate(dt)

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
           self.rotate(-dt)

        if keys[pygame.K_SPACE]:
           if self.cooldownTimer > 0:
               self.cooldownTimer -= dt
               return
           self.shoot()
           self.cooldownTimer = 0.3
           
               

    def shoot(self):
        fire = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        fire.velocity = pygame.Vector2(0,1)
        fire.velocity = fire.velocity.rotate(self.rotation)
        fire.velocity *= PLAYER_SHOOT_SPEED
