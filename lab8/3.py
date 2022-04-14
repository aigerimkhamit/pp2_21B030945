import random
import pygame
import math

BLACK = (0, 0, 0)
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Paint')
screen.fill(BLACK)
base = pygame.Surface((800, 600))

draw_on = False

pos_last = (0, 0)

colors = {
    'red' : (255, 0, 0),
    'blue' : (0, 0, 255),
    'green' : (0, 255, 0),
    'white' : (255, 255, 255)
}

color = colors['white']
figure = 'pen'

def Rect_pos(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                color = colors['blue']
            if event.key == pygame.K_g:
                color = colors['green']
            if event.key == pygame.K_r:
                color = colors['red']
            if event.key == pygame.K_w:
                color = colors['white']
            if event.key == pygame.K_p:
                figure = 'pen'
            if event.key == pygame.K_c:
                figure = 'circle'
            if event.key == pygame.K_k:
                figure = 'rectangle'
            if event.key == pygame.K_e:
                figure = 'erase'
        if event.type == pygame.MOUSEBUTTONDOWN:
            draw_on = True
            pos_last = event.pos
        if event.type == pygame.MOUSEBUTTONUP:
            draw_on = False
            base.blit(screen, (0, 0))
        if event.type == pygame.MOUSEMOTION:
            if draw_on == True:
                if figure == 'circle':
                    screen.blit(base, (0, 0))
                    pygame.draw.circle(screen, color, (pos_last[0], pos_last[1]), int(math.sqrt((event.pos[0] - pos_last[0]) ** 2 + (event.pos[1] - pos_last[1]) ** 2)))
                if figure == 'rectangle':
                    screen.blit(base, (0, 0))
                    a = Rect_pos(pos_last[0], pos_last[1], event.pos[0], event.pos[1])
                    pygame.draw.rect(screen, color, pygame.Rect(a))
                if figure == 'pen':
                    pygame.draw.line(screen, color, [pos_last[0], pos_last[1]], [event.pos[0], event.pos[1]], 5)
                    pos_last = event.pos
                if figure == 'erase':
                    pygame.draw.circle(screen, BLACK, (event.pos[0], event.pos[1]), 9)
    pygame.display.flip()
pygame.quit()


            

            