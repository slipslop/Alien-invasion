import pygame.font
class Button():
    def __init__(self,game,msg,x,y):
        self.screen = game.screen
        self.screenRect = game.screen.get_rect()

        #dimensions and properties of button
        
        self.width, self.height = 200, 50
        self.buttonColor = (0,255,0)
        self.textColor = (255,255,255)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(x,y,self.width,self.height)
        #self.rect.center = self.screenRect.center
        self._prepMsg(msg)

    def _prepMsg(self,msg):
        """turn given msg into a rendered image and center text on the button """
        self.msgImage = self.font.render(msg,True,self.textColor,self.buttonColor)
        self.msgImageRect = self.msgImage.get_rect()
        self.msgImageRect.center = self.rect.center
    
    def drawButton(self):
        # draw blank button and then draw message
        self.screen.fill(self.buttonColor,self.rect)
        self.screen.blit(self.msgImage,self.msgImageRect)