import pygame
pygame.init()
screen = pygame.display.set_mode((400,500))
screen.fill("white")
running = True

pygame.draw.circle(screen, "red", (300,400), 10, 50)
pygame.draw.circle(screen, "red", (100,400), 50, 3)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    pygame.display.flip()





