import pygame
pygame.init()
screen = pygame.display.set_mode((400,500))
screen.fill("blue")
running = True

rectangle = pygame.draw.rect(screen,"red",pygame.Rect(30,30,60,60))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    pygame.display.flip()