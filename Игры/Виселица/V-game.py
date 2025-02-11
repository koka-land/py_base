import pygame
import sys

pygame.init()

# Настройки экрана
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Простая игра на Pygame")

# Цвета
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Позиция квадрата
x, y = 400, 300
speed = 5

# Основной цикл игры
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if x >= 0:
            x -= speed
    if keys[pygame.K_RIGHT]:
        if x <= 750:
            x += speed
    if keys[pygame.K_UP]:
        if y >= 0:
            y -= speed
    if keys[pygame.K_DOWN]:
        if y <= 550:
            y += speed
    if keys[pygame.K_r]:
        x, y = 400, 300


    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (x, y, 50, 50))
    pygame.display.flip()
    pygame.time.Clock().tick(30)