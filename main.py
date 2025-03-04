import pygame
import random

# Initialize pygame
pygame.init()

# Game constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pixel Space Fury")

# Load assets
player_img = pygame.image.load("player.png")  # Add your spaceship image
enemy_img = pygame.image.load("enemy.png")    # Add your enemy image
bullet_img = pygame.image.load("bullet.png")  # Add your bullet image

# Scale images
player_img = pygame.transform.scale(player_img, (50, 50))
enemy_img = pygame.transform.scale(enemy_img, (40, 40))
bullet_img = pygame.transform.scale(bullet_img, (10, 20))

# Classes
class Player:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT - 70
        self.speed = 5
        self.bullets = []

    def move(self, dx):
        self.x = max(0, min(WIDTH - 50, self.x + dx))

    def shoot(self):
        bullet = Bullet(self.x + 20, self.y)
        self.bullets.append(bullet)

    def draw(self):
        screen.blit(player_img, (self.x, self.y))
        for bullet in self.bullets:
            bullet.move()
            bullet.draw()

class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = -7

    def move(self):
        self.y += self.speed

    def draw(self):
        screen.blit(bullet_img, (self.x, self.y))

class Enemy:
    def __init__(self):
        self.x = random.randint(0, WIDTH - 40)
        self.y = random.randint(-100, -40)
        self.speed = random.randint(2, 4)

    def move(self):
        self.y += self.speed

    def draw(self):
        screen.blit(enemy_img, (self.x, self.y))

# Game loop
player = Player()
enemies = [Enemy() for _ in range(5)]
clock = pygame.time.Clock()
running = True

while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move(-player.speed)
    if keys[pygame.K_RIGHT]:
        player.move(player.speed)
    if keys[pygame.K_SPACE]:
        player.shoot()

    player.draw()
    for enemy in enemies:
        enemy.move()
        enemy.draw()
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
