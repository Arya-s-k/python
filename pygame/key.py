import pygame
pygame.init()
x = 160
y = 100
screen = pygame.display.set_mode((400,500))

done = False

while not done:
    
    screen.fill((123,123,123))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            y = y - 5
        if pressed[pygame.K_DOWN]:
            y = y + 5 
        if pressed[pygame.K_LEFT]:
            x = x - 5
        if pressed[pygame.K_RIGHT]:
            x = x + 5
    pygame.draw.rect(screen,"red",(x,y,10,20))
            
            
    pygame.display.flip()