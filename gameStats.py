class GameStats():
    def __init__(self,game):
        self.settings = game.settings
        self.resetStats()
        self.gameActive = False
        self.practiceActive = False
        self.score = 0
        self.highscore = 0
        self.readHighscore()

    def resetStats(self):
        self.shipsLeft = self.settings.shipLimit
        self.score = 0

    def writeHighscore(self):
        with open("highscore.txt", "r+") as file:
            data = file.read()
            file.seek(0)
            if(data):
                if(self.highscore > int(data)):
                    file.write(str(self.highscore))
                else:
                    return False
            else:
                #there was nothing in the file...
                file.write(str(self.highscore))
           
    def readHighscore(self):
        file = open("highscore.txt","r")
        a = file.read()
        if(a):
            self.highscore = int(a)
        else:
            return False