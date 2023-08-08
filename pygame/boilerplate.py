import pygame
import sys

# General setup
pygame.init()
clock = pygame.time.Clock()

# Game_screen
WIDTH = 1024
HEIGHT = 1024
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Enter title here")


# event loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(60)
