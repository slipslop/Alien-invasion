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
        self.prepHighscore()


    def prepScore(self):
        """ turn score into rendered image """
                # turn it to string
        scoreStr = str(self.stats.score)
        self.scoreImage = self.font.render(scoreStr,True,self.textColor,self.settings.backgroundColor)
        
        # display score at top right
        self.scoreRect = self.scoreImage.get_rect()
        self.scoreRect.right = self.screenRect.right - 20
        self.scoreRect.top = 20

    def prepHighscore(self):
        """ turn score into rendered image """
        # turn it to string
        highscoreStr = str(self.stats.highscore)
        self.highscoreImage = self.font.render(highscoreStr,True,self.textColor,self.settings.backgroundColor)
        
        # display score at top right
        self.highscoreRect = self.highscoreImage.get_rect()
        self.highscoreRect.centerx = self.screenRect.centerx
        self.highscoreRect.top = self.scoreRect.top
    
    def checkHighScore(self):
        """ check to see if there is a new high score """
        if self.stats.score > self.stats.highscore:
            self.stats.highscore = self.stats.score
            self.prepHighscore()
    
    def showScore(self):
        """ draw the score on the screen """
                        # what we draw, where we draw
        self.screen.blit(self.scoreImage,self.scoreRect)
        self.screen.blit(self.highscoreImage,self.highscoreRect)