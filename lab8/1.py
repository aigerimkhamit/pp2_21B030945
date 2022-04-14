import random, time
import sys

import pygame
from pygame.locals import *

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()
# colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(WHITE)
pygame.display.set_caption('GAME')
background = pygame.image.load('AnimatedStreet.png')

font = pygame.font.SysFont('Verdana', 60)
font1 = pygame.font.SysFont('Verdana', 14)
font_small = pygame.font.SysFont('Verdana', 20)
game_over = font.render("Game Over", True, BLACK)
collected_coins = font1.render("Collected coins = ", True, BLACK)
# screen.blit(collected_coins, (0, 0))


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Enemy.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        self.rect.move_ip(0, 10)
        if self.rect.bottom > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Player.png')
        self.rect = self.image.get_rect()
        self.rect.center = (100, 560)

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-10, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(10, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

coin_speed = 5
score = 0
score_font = pygame.font.SysFont('Verdana', 14)
def show_score(x, y):
    global score
    s = score_font.render(f'{score}', True, BLACK)
    screen.blit(s, (x, y))

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.smoothscale(pygame.image.load('coin.png'), (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - 50)
        self.rect.y = 0
    def move(self):
        global score
        self.rect.y += coin_speed
        # collision with coin
        if pygame.Rect.collidepoint(P1.rect, self.rect.x, self.rect.y):
            score += 1
            self.rect.top = 0
            pygame.mixer.Sound('coinsound.mp3').play()
            self.rect.x = random.randint(0, SCREEN_WIDTH - 50)
            self.rect.y = 0
        
        if (self.rect.y > SCREEN_HEIGHT - 50):
            self.rect.x = random.randint(0, SCREEN_WIDTH - 50)
            self.rect.y = 0
        
    def draw(self, surface):
        surface.blit(self.image, self.rect)


P1 = Player()
E1 = Enemy()
F1 = Coin()

#Creating Sprites Groups
coins_list = [Coin()]
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # collision with enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound('crash.wav').play()
          time.sleep(0.1)
                    
          screen.fill(RED)
          screen.blit(game_over, (30,250))
           
          pygame.display.update()
          for entity in all_sprites: 
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()

    P1.update()
    E1.move()
    F1.move()

    screen.fill(WHITE)
    screen.blit(background, (0, 0))
    P1.draw(screen)
    E1.draw(screen)
    
    F1.draw(screen)
    screen.blit(collected_coins, (245, 0))
    show_score(370, 0)
    pygame.display.update()
    FramePerSec.tick(FPS)
