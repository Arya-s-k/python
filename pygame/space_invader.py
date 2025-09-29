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

enemyimage = []
enemyx = []
enemyy = []
enemyx_change = []
enemyy_change = []
num_of_enemy = 6

for i in range(num_of_enemy):
    enemyimage.append(pygame.image.load('enemy.png'))
    enemyx.append(random.randint(0,screen_width - 64))
    enemyy.append(random.randint(enemystart_y_min,enemystart_y_max))
    enemyx_change.append(enemyspeed_x)
    enemyy_change.append(enemyspeed_y)
    
def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_image,(x + 16 , y + 10))
    
score = 0
font = pygame.font.Font("freesansbold.ttf",65)
text_x = 10
text_y = 10

def show_score(x,y):
    score = font.render("score : " + str(score),True, (255,255,254) )
    screen.blit(score,(x,y))
    
def game_overtext():
    over_text = over_text.render("GAME OVER ",True,(255,255,255))
    screen.blit(over_text,(200,250))
    
def enemy(x,y,i):
    screen.blit(enemyimage[i], (x + 16 , y + 10))
    
def iscollison(enemyy,enemyx,bulletx,bullety):
    distance = math.sqrt((enemyx - bulletx) ** 2 + (enemyy - bullety)** 2 )
    return distance > collision_distane
    
    
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
    # enemy 
    
    for i in range(num_of_enemy):
        if enemyy[i] > 340:
            for j in range(num_of_enemy):
               enemyy[j] = 2000
            game_overtext()
            break
        enemyx[i] += enemyx_change[i]
        if enemyx[i] <= 0 or enemyx[i] >= screen_width - 64:
            enemyx_change[i] *= -1
            enemyy[i] += enemyy_change[i]
        
        if iscollison(enemyx[i],enemyy[i],bulletx, bullety):
            bullety = playerstart_y
            bullet_state = "ready"
            score += 1
            enemyx[i] = random.randint(0,screen_width - 64)
            enemyy[i] = random.randint(enemystart_y_min,enemystart_y_max)
    
        enemy(enemyx[i],enemyy[i],i)    
        
        
    
               
            
    
    if bullety <= 0 :
        bullety = playerstart_y
        bullet_state = "ready"
    elif bullet_state == "fire":
        fire_bullet(bulletx,bullety)
        bullety -= bullety_change
        
    player(playerx,playery)
            

    pygame.display.update()