class GameStats():
    def __init__(self,game):
        self.settings = game.settings
        self.resetStats()
        self.gameActive = False

    def resetStats(self):
        self.shipsLeft = self.settings.shipLimit