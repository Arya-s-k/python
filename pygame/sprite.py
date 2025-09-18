import pygame
import random
pygame.init
width = 400
length =500

screen_resolution = (width,length)
screen = pygame.display.set_caption("bouncing ball")
screen = pygame.display.set_mode((screen_resolution))
colours = ['Red','Blue','Orange','Cyan','Teal','Yellow']
x = 100 
y = 100

bgcolour = 'Red'
rect_obj = pygame.draw.rect(screen,"blue",pygame.Rect(x,y,40,40))
speed = [1,-1]
clr = random.choice(colours)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    screen.fill(bgcolour)
    
    rect_obj = rect_obj.move (speed)
    
    if  rect_obj.left <= 0 or rect_obj.right >= width:
        speed[0] = -speed[0]
        clr = random.choice(colours)
        bgcolour = random.choice(colours)
    if  rect_obj.top <= 0 or rect_obj.bottom >= length:
        speed[1] = -speed[1]
        clr = random.choice(colours)
        bgcolour = random.choice(colours)
        
    rect_obj= pygame.draw.rect(screen,clr,pygame.Rect(rect_obj.x,rect_obj.y,40,40))
    
    pygame.display.flip()
    
    