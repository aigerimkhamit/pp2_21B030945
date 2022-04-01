import pygame
from datetime import datetime

size = width, height = (800, 600)
screen = pygame.display.set_mode(size)

background = pygame.transform.scale(pygame.image.load('mickey.jpg'), (800, 600))
sec = pygame.transform.smoothscale(pygame.image.load('mickeysec.png'), (800, 600))
min = pygame.transform.smoothscale(pygame.image.load('mickeymin.png'), (800, 600))
clock = pygame.time.Clock()

def r_center(s,image, angle, x, y): 
    r_image = pygame.transform.rotate(image, angle) 
    n_rect = r_image.get_rect(center = image.get_rect(center = (x, y)).center) 
    s.blit(r_image,n_rect)

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.blit(background, (0, 0))
    time = datetime.now()
    clock.tick(30)
    r_center(screen, sec, -time.second * 6, 400, 300)
    r_center(screen, min, -time.minute * 6 - 42, 400, 300)
    pygame.display.update()
pygame.quit()