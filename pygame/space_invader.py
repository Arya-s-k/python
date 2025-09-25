import math
import random
import pygame

screen_width = 800
screen_height = 500
playerstart_x = 370
playerstart_y = 380

enemystart_y_min = 50
enemystart_y_max = 150
enemyspeed_x = 4
enemyspeed_y = 40
bullet_speed_y  = 10
collision_distane = 27

pygame.init()

screen = pygame.display.set_mode((screen_width,screen_height))

background = pygame.image.load('background.png')

player_image = pygame.image.load('player.png')
playerx = playerstart_x
playery = playerstart_y
playerx_change = 0 

def player(x,y):
    screen.blit(player_image,(x,y))
    
bullet_image = pygame.image.load('bullet.png')
bulletx = 0 
bullety = playerstart_y
bulletx_change = 0 
bullety_change = bullet_speed_y
bullet_state = "ready"


def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_image,(x + 16 , y + 10))
running = True
while running:
    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            playerx_change = -5 
        if pressed[pygame.K_RIGHT]:
            playerx_change = 5 
        if pressed[pygame.K_SPACE ] and bullet_state == "ready":
            bulletx = playerx
            fire_bullet(bulletx,bullety)
        if event.type == pygame.KEYUP and event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
            playerX_change = 0
    playerx += playerx_change 
    playerx = max(0,min(playerx,screen_width - 64))
    if bullety <= 0 :
        bullety = playerstart_y
        bullet_state = "ready"
    elif bullet_state == "fire":
        fire_bullet(bulletx,bullety)
        bullety -= bullety_change
        
    player(playerx,playery)
            

    pygame.display.update()