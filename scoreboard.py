import pygame.font
class Scoreboard:
    def __init__(self,game):
        """ keeps track of score """
        self.screen = game.screen
        self.screenRect = self.screen.get_rect()
        self.settings = game.settings
        self.stats = game.stats
        
        #font settings
        self.textColor = (30,30,30)
        self.font = pygame.font.SysFont(None,48)

        #prepare initial score image
        self.prepScore()


    def prepScore(self):
        """ turn score into rendered image """
                # turn it to string
        scoreStr = str(self.stats.score)
        self.scoreImage = self.font.render(scoreStr,True,self.textColor,self.settings.backgroundColor)
        
        # display score at top right
        self.scoreRect = self.scoreImage.get_rect()
        self.scoreRect.right = self.screenRect.right - 20
        self.scoreRect.top = 20
    
    def showScore(self):
        """ draw the score on the screen """
                        # what we draw, where we draw
        self.screen.blit(self.scoreImage,self.scoreRect)