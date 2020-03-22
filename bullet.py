import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    def __init__(self,game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.color = self.settings.bulletColor

        self.rect = pygame.Rect(0,0,self.settings.bulletWidth,self.settings.bulletHeight)
        self.rect.midtop = game.ship.rect.center
        self.rect.x = 100
        self.x = float(self.rect.x)

    def update(self):
        self.x += self.settings.bulletSpeed
        self.rect.x = self.x
    def blitme(self):
        pygame.draw.rect(self.screen,self.color,self.rect)