import pygame
from pygame.sprite import Sprite
class TargetPractice(Sprite):
    def __init__(self,game):
        super().__init__()
        ''' basically just draws a green square that moves
        up and down '''
        self.screen = game.screen
        self.settings = game.settings
        self.color = self.settings.practiceTargetColor
        self.screenRect = self.screen.get_rect()
        #create target rect
        self.rect = pygame.Rect(self.settings.screenHeight / 2,self.settings.screenWidth / 2
                                ,self.settings.practiceTargetWidth,
                                self.settings.practiceTargetHeight)
        self.y = float(self.rect.y)

    def update(self):
        #start at center? move down until bottom and start going
        # up until at the top and repeat
        # speed * direction ? e.g 3 * -1 = -3 and 3 * 1 = 3
        self.y -= (self.settings.practiceTargetDirection * self.settings.practiceTargetSpeed)
        self.rect.y = self.y
        #if(self.rect.y < self.settings.screenHeight or self.rect.y > self.settings.screenHeight):
        if self.rect.bottom >= self.screenRect.bottom or self.rect.top <= self.screenRect.top:
            self.settings.practiceTargetDirection *= -1
            print("changed direction") 




    def drawPracticeTarget(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
