import pygame
pygame.init()
screen = pygame.display.set_mode((400,400))
image = pygame.image.load("arya.jpg").convert()
bg = pygame.transform.scale(image,(400,400))
penguin = pygame.image.load("1092433.png").convert()
bg2 = pygame.transform.scale(image,(100,100))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        screen.blit(bg,(0,0))
        screen.blit(bg,(200,200))
        
        
    pygame.display.flip()