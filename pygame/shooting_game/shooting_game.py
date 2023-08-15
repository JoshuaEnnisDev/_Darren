import pygame
import sys
from random import randint


# classes
class Crosshair(pygame.sprite.Sprite):
    def __init__(self, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.gun_sound = pygame.mixer.Sound('sounds/gunshot.wav')

    def shoot(self):
        self.gun_sound.play()
        pygame.sprite.spritecollide(crosshair, target_group, True)

    def update(self):
        self.rect.center = pygame.mouse.get_pos()


class Target(pygame.sprite.Sprite):
    def __init__(self, image_path, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)


# general setup
pygame.init()
clock = pygame.time.Clock()

# game_screen
WIDTH = 1024
HEIGHT = 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Target Practice")

pygame.mouse.set_visible(False)

# crosshair
crosshair = Crosshair("graphics/crosshair.png")
crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)

# target
target_group = pygame.sprite.Group()
for _ in range(20):
    target_group.add(Target('graphics/target.png', randint(20, WIDTH), randint(0, HEIGHT)))


# event loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            crosshair.shoot()
    screen.fill((150, 200, 100))
    target_group.draw(screen)
    crosshair_group.draw(screen)
    crosshair_group.update()
    pygame.display.update()
    clock.tick(60)
