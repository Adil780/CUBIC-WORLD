import pygame, cubic
pygame.init()

group = pygame.sprite.Group()
for i in range(50, 700, 52):
    a = cubic.Cub(i + 70, i + 52)
    group.add(a)


n = 750
for i in range(724, 100, -52):
    n += 52
    i -= 52
    a = cubic.Cub(n, i)
    group.add(a)

