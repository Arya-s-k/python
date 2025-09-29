import pygame
import random
import time

pygame.init()
width = 400
length = 500

screen_resolution = (width, length)
pygame.display.set_caption("Two Bouncing Rectangles")
screen = pygame.display.set_mode(screen_resolution)

colours = ['Red', 'Blue', 'Orange', 'Cyan', 'Teal', 'Yellow', 'Green', 'Purple', 'White']

x1 = 100
y1 = 100
speed1 = [1, -1]
clr1 = random.choice(colours)
rect_size = 40
rect_obj1 = pygame.Rect(x1, y1, rect_size, rect_size)

x2 = 300
y2 = 350
speed2 = [-1, 1]
clr2 = random.choice(colours)
rect_obj2 = pygame.Rect(x2, y2, rect_size, rect_size)

bgcolour = 'Black'

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill(bgcolour)

    rect_obj1 = rect_obj1.move(speed1)

    if rect_obj1.left <= 0 or rect_obj1.right >= width:
        speed1[0] = -speed1[0]
        clr1 = random.choice(colours)
    if rect_obj1.top <= 0 or rect_obj1.bottom >= length:
        speed1[1] = -speed1[1]
        clr1 = random.choice(colours)

    rect_obj2 = rect_obj2.move(speed2)

    if rect_obj2.left <= 0 or rect_obj2.right >= width:
        speed2[0] = -speed2[0]
        clr2 = random.choice(colours)
        bgcolour = random.choice(colours)
    if rect_obj2.top <= 0 or rect_obj2.bottom >= length:
        speed2[1] = -speed2[1]
        clr2 = random.choice(colours)
        bgcolour = random.choice(colours)

    pygame.draw.rect(screen, clr1, rect_obj1)

    pygame.draw.rect(screen, clr2, rect_obj2)

    pygame.display.flip()

    clock.tick(60)