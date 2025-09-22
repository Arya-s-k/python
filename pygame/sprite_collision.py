import pygame
pygame.init()
width = 500 
height = 400
screen = pygame.display.set_mode((width,height))
screen.fill("blue")
mspeed  = 1 
font = pygame.font.SysFont("times new roman",72)

class Sprite(pygame.sprite.Sprite):
    def __init__(self,color,h,w):
        super().__init__()
        self.image = pygame.Surface([h,w])
        self.image.fill(color)
        self.rect = self.image.get_rect()
    def move(self,xchange,ychange):
        self.rect.x = max(min(self.rect.x +xchange ,width -self.rect.w),0)
        self.rect.y = max(min(self.rect.y +ychange ,width -self.rect.h),0)
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()  
sprite1 = Sprite("green",20,20)
sprite1.rect.x = 200
sprite1.rect.y = 200
all_sprites.add(sprite1)

sprite2 = Sprite("red",20,20)
sprite2.rect.x = 100
sprite2.rect.y = 50
all_sprites.add(sprite2)

while True:
    screen.fill("black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    keys = pygame.key.get_pressed()
    xchange = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * mspeed
    ychange = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * mspeed
    if sprite1.rect.colliderect(sprite2.rect):

        win_text = font.render("you win",True,pygame.Color("yellow"))
        screen.blit(win_text,(200,200))
        all_sprites.remove(sprite2)
        
    sprite1.move(xchange,ychange)
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(90)