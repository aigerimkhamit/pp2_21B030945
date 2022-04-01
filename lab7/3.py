import pygame 
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

size = width, height = (750, 750)

screen = pygame.display.set_mode(size)

pygame.display.set_caption('Circle')

clock = pygame.time.Clock()

circle_x = 0
circle_y = 0
circle_change_x = 20
circle_change_y = 20

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        # if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
        #     circle_y -= circle_change_y
        # if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
        #     circle_y += circle_change_y
        # if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
        #     circle_x -= circle_change_x
        # if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
        #     circle_x += circle_change_x
    
    if circle_x > 700 or circle_x < 0:
        circle_change_x *= -1
    if circle_y > 700 or circle_y < 0:
        circle_change_y *= -1

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        circle_y -= circle_change_y
    if pressed[pygame.K_DOWN]:
        circle_y += circle_change_y
    if pressed[pygame.K_LEFT]:
        circle_x -= circle_change_x
    if pressed[pygame.K_RIGHT]:
        circle_x += circle_change_x

    screen.fill(WHITE)
    pygame.draw.ellipse(screen, RED, [circle_x, circle_y, 50, 50])

    clock.tick(60)
    pygame.display.update()
pygame.quit()