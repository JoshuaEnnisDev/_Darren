import pygame
import sys

# General setup
pygame.init()
clock = pygame.time.Clock()

# Game_screen
WIDTH = 1024
HEIGHT = 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Enter title here")

# test_surf = pygame.Surface((50, 50))
# test_surf.fill("black")
# test_rect = test_surf.get_rect(center=(100, 100))
test_image = pygame.image.load('graphics/crosshair.png')
test_rect = test_image.get_rect(center=(100, 100))

# event loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((150, 200, 100))
    screen.blit(test_image, test_rect)
    test_rect.x += 1
    pygame.display.update()
    clock.tick(60)
