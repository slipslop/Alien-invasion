import pygame.font
class Button():
    def __init__(self,game,msg):
        self.screen = game.screen
        self.screenRect = game.screen.get_rect()

        #dimensions and properties of button
        
