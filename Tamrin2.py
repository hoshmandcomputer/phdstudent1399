import pygame
import random
import numpy
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
BLUE  = (  0,   0, 255)
#------------------------------------- 
class Block(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        self.image = pygame.Surface([20, 15])
        self.image.fill(color)
        self.rect = self.image.get_rect()
#-------------------------------------         
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
#-------------------------------------         
class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([4, 10])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.y -= 3
#-------------------------------------        
        
pygame.init()
screen = pygame.display.set_mode([700, 400])

all_sprites_list = pygame.sprite.Group()
block_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()
X=[]
for i in range(10):
    block = Block(BLUE)
    block.rect.x = random.randrange(700)
    block.rect.y = random.randrange(350)
    block_list.add(block)
    all_sprites_list.add(block)
    X.append(block.rect.x )###########

sort_val_X=sorted(X)
sort_index_X=numpy.argsort(X)

print(sort_val_X)
print(sort_index_X)

print(block_list.sprites()[sort_index_X[0]].rect.x)