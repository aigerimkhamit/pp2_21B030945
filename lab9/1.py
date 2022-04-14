import random, time
import sys

import pygame
from pygame.locals import *

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

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

speed = 10
coin_speed = 5
score = 0
score_font = pygame.font.SysFont('Verdana', 14)
def show_score(x, y):
    global score
    s = score_font.render(f'{score}', True, BLACK)
    screen.blit(s, (x, y))

class Enemy(pygame.sprite.Sprite):
    global speed, score
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Enemy.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        speed = 5
        if score >= 30:
            speed = 15
        self.rect.move_ip(0, speed)
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
        self.x = SCREEN_WIDTH / 2
        self.y = SCREEN_HEIGHT - 50
        self.rect.center = (self.x, self.y)

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.x += -5
                self.rect.move_ip(-10, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.x += 5
                self.rect.move_ip(10, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

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


class Coin1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image1 = pygame.transform.smoothscale(pygame.image.load('coin.png'), (60, 60))
        self.rect1 = self.image1.get_rect()
        self.rect1.x = random.randint(50, SCREEN_WIDTH - 50)
        self.rect1.y = 0

    def move(self):
        global score
        self.rect1.y += coin_speed 
        if pygame.Rect.collidepoint(P1.rect, self.rect1.x, self.rect1.y):
            score += 3
            self.rect1.top = 0
            pygame.mixer.Sound('coinsound1.wav').play()
            self.rect1.x = random.randint(50, SCREEN_WIDTH - 50)
            self.rect1.y = 0

        if (self.rect1.y > SCREEN_HEIGHT - 50):
                self.rect1.x = random.randint(50, SCREEN_WIDTH - 50)
                self.rect1.y = 0

    def draw(self, surface):
        surface.blit(self.image1, self.rect1)

P1 = Player()
E1 = Enemy()
F1 = Coin()
F2 = Coin1()

#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
# coins = pygame.sprite.Group()
# coins.add(F1)
# all_coins = pygame.sprite.Group()
# all_coins.add(P1)
# all_coins.add(F1)

# showing score
score = 0
score_font = pygame.font.SysFont('Verdana', 14)
def show_score(x, y):
    global score
    s = score_font.render(f'{score}', True, BLACK)
    screen.blit(s, (x, y))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

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
    if score % 10 == 0 and score != 0:
        F2.move()
    screen.fill(WHITE)
    screen.blit(background, (0, 0))
    P1.draw(screen)
    E1.draw(screen)
    F1.draw(screen)
    if score % 10 == 0 and score != 0:
        F2.draw(screen)
    
    screen.blit(collected_coins, (245, 0))
    show_score(370, 0)
    pygame.display.update()
    FramePerSec.tick(FPS)
