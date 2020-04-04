class Settings:
    def __init__(self):
        self.screenWidth = 1200
        self.screenHeight = 800
        self.backgroundColor = (0,0,125)

        self.shipSpeed = 4

        self.bulletColor = (200,200,200)
        self.bulletHeight = 3
        self.bulletWidth = 15
        self.bulletSpeed = 6
        self.allowedBulletAmount = 3

        self.alienSpeedX = 0.4
        #1 = up, -1 = down
        self.alienMovementDirection = 1
        self.alienDropSpeed = -40
        self.alienPoints = 50

        self.shipLimit = 3

        self.practiceTargetSpeed = 1
        self.practiceTargetHeight = 60
        self.practiceTargetWidth = 60
        self.practiceTargetColor = (100,100,100)
        #-1 down , 1 up
        self.practiceTargetDirection = -1
        self.bulletsAvailable = 3
    
    def resetSettings(self):
        #resets all vital settings back. You need to maintain these...
        self.shipSpeed = 4
        self.bulletSpeed = 6
        self.allowedBulletAmount = 3
        self.alienSpeedX = 0.4
        #1 = up, -1 = down
        self.alienMovementDirection = 1
        self.alienDropSpeed = -40
        self.shipLimit = 3
        self.practiceTargetSpeed = 1
        #-1 down , 1 up
        self.practiceTargetDirection = -1
        self.bulletsAvailable = 3
    
    def makePracticeTargetHarder(self):
        self.practiceTargetSpeed += 0.5
        self.practiceTargetHeight * 0.9
        self.practiceTargetWidth * 0.9