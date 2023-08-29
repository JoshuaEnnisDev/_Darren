import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)
        self.image = pygame.image.load('../graphics/test/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)

        self.direction = pygame.math.Vector2()
        self.speed = 5

        self.obstacle_sprites = obstacle_sprites

    def input(self):
        keys = pygame.key.get_pressed()
        
        self.direction = pygame.math.Vector2((
            keys[pygame.K_d] - keys[pygame.K_a],
            keys[pygame.K_s] - keys[pygame.K_w])
        )

        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        # if keys[pygame.K_UP]:
        #     self.direction.y = -1
        # elif keys[pygame.K_DOWN]:
        #     self.direction.y = 1
        # else:
        #     self.direction.y = 0

        # if keys[pygame.K_LEFT]:
        #     self.direction.x = -1
        # elif keys[pygame.K_RIGHT]:
        #     self.direction.x = 1
        # else:
        #     self.direction.x = 0

    def move(self, speed):
        # self.rect.center += self.direction * speed
        self.rect.x += self.direction.x * speed
        self.collision('horizontal')

        self.rect.y += self.direction.y * speed
        self.collision('vertical')

    def collision(self, direction):
        collision_list = pygame.sprite.spritecollide(self, self.obstacle_sprites, False)

        for sprite in collision_list:
            if direction == 'horizontal':
                if self.direction.x > 0:
                    self.rect.right = sprite.rect.left
                if self.direction.x < 0:
                    self.rect.left = sprite.rect.right

            if direction == 'vertical':
                if self.direction.y > 0:
                    self.rect.bottom = sprite.rect.top
                if self.direction.y < 0:
                    self.rect.top = sprite.rect.bottom

    def update(self):
        self.input()
        self.move(self.speed)

