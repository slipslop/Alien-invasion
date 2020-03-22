import pygame
class SpaceShip:
    def __init__(self,game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.settings = game.settings
        #load the image
        self.image = pygame.transform.scale(pygame.image.load('images/ship.bmp'),(100,50))
        self.rect = self.image.get_rect()
        #start new ship at the center left halfway from top
        print(self.settings.screenHeight)
        self.rect.y = self.screen_rect.centery

        self.y = self.rect.y
        self.movingUp = False
        self.movingDown = False
        self.speed = game.settings.shipSpeed


    def moveShip(self,game):
        if self.movingUp and self.rect.y > 0:
            print(self.rect.y)
            print(game.settings.screenHeight)
            self.y -= self.speed
        if self.movingDown and self.rect.y < (game.settings.screenHeight-50):
            self.y += self.speed
        self.rect.y = self.y
    
    def centerShip(self):
        self.rect.y = self.screen_rect.centery
        
    def blitme(self):
        self.screen.blit(self.image,self.rect)