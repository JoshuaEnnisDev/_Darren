import pygame
from pytmx.util_pygame import load_pygame
from settings import *
from tile import Tile
from player import Player
from debug import debug


class Level:
    def __init__(self):

        # get the display surface
        self.display_surface = pygame.display.get_surface()

        # sprite group setup
        self.ground_sprites = YSortCameraGroup(False)
        self.sorted_sprites = YSortCameraGroup(True)
        self.obstacle_sprites = pygame.sprite.Group()
        self.create_map()

    def create_map(self):
        tmxdata = load_pygame("../tmx/base-level.tmx")
        
        for layer in tmxdata.visible_layers:
            if layer.name in ["Floor", "Floor Details"]:
                for x, y, surf in layer.tiles():
                    pos = (x * TILESIZE, y * TILESIZE)
                    Tile(pos, surf, [self.ground_sprites])
            elif layer.name == "collisions":
                for x, y, surf in layer.tiles():
                    pos = (x * TILESIZE, y * TILESIZE)
                    Tile(pos, surf, [self.obstacle_sprites])
        for obj in tmxdata.objects:
            print(dir(obj))
            pos = (obj.x, obj.y) 
            Tile(pos, obj.image, [self.obstacle_sprites, self.sorted_sprites])
        self.player = Player((2000, 1430), [self.sorted_sprites], self.obstacle_sprites)

    def run(self):
        self.ground_sprites.custom_draw(self.player)
        self.ground_sprites.update()
        self.sorted_sprites.custom_draw(self.player)
        self.sorted_sprites.update()


class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self, ysort):
        super().__init__()
        self.ysort = ysort
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2

    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        if self.ysort:
            for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
                offset_pos = sprite.rect.topleft - self.offset
                self.display_surface.blit(sprite.image, offset_pos)
        else:
            for sprite in self.sprites():
                offset_pos = sprite.rect.topleft - self.offset
                self.display_surface.blit(sprite.image, offset_pos)

