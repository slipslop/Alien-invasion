class GameStats():
    def __init__(self,game):
        self.settings = game.settings
        self.resetStats()
        self.gameActive = False
        self.practiceActive = False
        self.score = 0

    def resetStats(self):
        self.shipsLeft = self.settings.shipLimit
        self.score = 0