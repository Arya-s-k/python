import math
import random
import pygame

screen_width = 800
screen_height = 500
playerstart_x = 370
playerstart_y = 380

enemystart_y_min = 50
enemystart_y_max = 150
enemyspeed_x = 2
enemyspeed_y = 40
bullet_speed_y = 10
collision_distance = 27

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Invaders")

background = pygame.image.load('background.png')

player_image = pygame.image.load('player.png')
playerx = playerstart_x
playery = playerstart_y
playerx_change = 0

def player(x, y):
    screen.blit(player_image, (x, y))

bullet_image = pygame.image.load('bullet.png')
bulletx = 0
bullety = playerstart_y
bullet_state = "ready"

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_image, (x + 16, y + 10))

enemy_image = pygame.image.load('enemy.png')
num_of_enemies = 7
enemyx = []
enemyy = []
enemyx_change = []
enemyy_change = []

for i in range(num_of_enemies):
    enemyx.append(random.randint(0, screen_width - 64))
    enemyy.append(random.randint(enemystart_y_min, enemystart_y_max))
    enemyx_change.append(enemyspeed_x)
    enemyy_change.append(enemyspeed_y)

def enemy(x, y, i):
    screen.blit(enemy_image, (x, y))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
    if distance < collision_distance:
        return True
    else:
        return False

running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerx_change = -5
            if event.key == pygame.K_RIGHT:
                playerx_change = 5
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bulletx = playerx
                fire_bullet(bulletx, bullety)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerx_change = 0

    playerx += playerx_change
    playerx = max(0, min(playerx, screen_width - 64))

    for i in range(num_of_enemies):
        enemyx[i] += enemyx_change[i]
        if enemyx[i] <= 0:
            enemyx_change[i] = enemyspeed_x
            enemyy[i] += enemyy_change[i]
        elif enemyx[i] >= screen_width - 64:
            enemyx_change[i] = -enemyspeed_x
            enemyy[i] += enemyy_change[i]

        collision = isCollision(enemyx[i], enemyy[i], bulletx, bullety)
        if collision:
            bullety = playerstart_y
            bullet_state = "ready"
            enemyx[i] = random.randint(0, screen_width - 64)
            enemyy[i] = random.randint(enemystart_y_min, enemystart_y_max)

        enemy(enemyx[i], enemyy[i], i)

    if bullety <= 0:
        bullety = playerstart_y
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletx, bullety)
        bullety -= bullet_speed_y

    player(playerx, playery)

    pygame.display.update()