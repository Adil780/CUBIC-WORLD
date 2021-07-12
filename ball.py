import pygame, settings, model, cubic

pygame.init()
from pygame.sprite import DirtySprite

class Ball(DirtySprite):
    BALL_WIDTH = 50
    BALL_HEIGHT = 50

    def __init__(self, posx, posy, speedx, speedy):
        DirtySprite.__init__(self)
        self.layer = 2
        self.speedx = speedx
        self.speedy = speedy
        self.image = pygame.Surface([self.BALL_WIDTH, self.BALL_HEIGHT], pygame.SRCALPHA)
        self.rect = pygame.Rect(posx, posy, self.BALL_WIDTH, self.BALL_HEIGHT)
        pygame.draw.circle(self.image, [255, 255, 255], [self.rect.width - self.BALL_WIDTH / 2, self.rect.height - self.BALL_HEIGHT / 2], self.BALL_WIDTH / 2)
        pygame.draw.circle(self.image, [0, 0, 0], [self.rect.width - self.BALL_WIDTH / 2, self.rect.height - self.BALL_HEIGHT / 2], self.BALL_WIDTH / 2, 4)

        print(1)

    def fly(self, cub):

        self.rect.x += self.speedx


        if self.rect.right >= settings.SCREEN_WIDTH:
            self.speedx = -self.speedx
            self.rect.right = settings.SCREEN_WIDTH

        if self.rect.left <= 0:
            self.speedx = -self.speedx
            self.rect.left = 0

        for i in cub:
            a = self.rect.colliderect(i)

            if a:
                if self.speedx > 0:
                    self.rect.right = i.rect.left
                    i.minus_hp(cub)

                elif self.speedx < 0:
                    self.rect.left = i.rect.right
                    i.minus_hp(cub)


                self.speedx = -self.speedx

        self.rect.y += self.speedy


        if self.rect.top <= 0:
            self.speedy = -self.speedy
            self.rect.top = 0


        if self.rect.bottom >= settings.SCREEN_HEIGHT:
            self.speedy = -self.speedy
            self.rect.bottom = settings.SCREEN_HEIGHT


        for b in cub:
            c = self.rect.colliderect(b)

            if c:
                if self.speedy < 0:
                    self.rect.top = b.rect.bottom
                    b.minus_hp(cub)
                if self.speedy > 0:
                    self.rect.bottom = b.rect.top
                    b.minus_hp(cub)

                self.speedy = -self.speedy




