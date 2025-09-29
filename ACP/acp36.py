import pygame

pygame.init()
width = 500
height = 400
screen = pygame.display.set_mode((width, height))
screen.fill("blue")
mspeed = 3
font = pygame.font.SysFont("times new roman", 48)

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, w, h):
        super().__init__()
        self.image = pygame.Surface([w, h])
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def move(self, xchange, ychange):
        self.rect.x = max(min(self.rect.x + xchange, width - self.rect.w), 0)
        self.rect.y = max(min(self.rect.y + ychange, height - self.rect.h), 0)

clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()

sprite1 = Sprite("green", 20, 20)
sprite1.rect.x = 200
sprite1.rect.y = 200
all_sprites.add(sprite1)

sprite2 = Sprite("red", 20, 20)
sprite2.rect.x = 100
sprite2.rect.y = 50
all_sprites.add(sprite2)

game_over = False

while True:
    screen.fill("black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()

    # Sprite 1 Movement (Arrow Keys)
    xchange1 = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * mspeed
    ychange1 = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * mspeed
    sprite1.move(xchange1, ychange1)

    # Sprite 2 Movement (WASD Keys)
    if not game_over:
        xchange2 = (keys[pygame.K_d] - keys[pygame.K_a]) * mspeed
        ychange2 = (keys[pygame.K_s] - keys[pygame.K_w]) * mspeed
        sprite2.move(xchange2, ychange2)

    # Collision Check
    if sprite1.rect.colliderect(sprite2.rect) and not game_over:
        game_over = True
        all_sprites.remove(sprite2)

    all_sprites.draw(screen)

    if game_over:
        win_text = font.render("YOU WIN!", True, pygame.Color("yellow"))
        text_rect = win_text.get_rect(center=(width // 2, height // 2))
        screen.blit(win_text, text_rect)

    pygame.display.flip()
    clock.tick(90)