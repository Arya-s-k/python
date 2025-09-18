import pygame
pygame.init()
screen = pygame.display.set_mode((400, 500))
screen.fill("white")
pygame.display.set_caption('My Pygame')
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('my pygame', True, "black")
pygame.draw.circle(screen, "red", (300, 400), 10)
pygame.draw.circle(screen, "red", (100, 400), 50, 3)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(text, (50, 50))
    pygame.display.flip()
pygame.quit()
