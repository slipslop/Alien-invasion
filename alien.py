import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    def __init__(self,game):
        super().__init__()
        self.screen = game.screen
        self.screenRect = game.screen.get_rect()

        self.image = pygame.transform.scale(pygame.image.load('images/alien.bmp'),(50,50))
        self.rect = self.image.get_rect()
        self.rect.x = game.settings.screenWidth - 100
        self.rect.y = 0

        self.x = float(self.rect.x)
    
    def checkEdges(self):
        if self.rect.bottom >= self.screenRect.bottom or self.rect.top <= self.screenRect.top:
            return True

    def update(self,game):
        self.y += game.settings.alienSpeedX * game.settings.alienMovementDirection
        self.rect.y = self.y
    