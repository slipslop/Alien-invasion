import sys
import pygame
from time import sleep
from settings import Settings
from spaceShip import SpaceShip
from bullet import Bullet
from alien import Alien
from gameStats import GameStats

class alienInvasionSideways():
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screenWidth,self.settings.screenHeight))
        pygame.display.set_caption("Alien invasion... Sideways")
        self.stats = GameStats(self)
        self.ship = SpaceShip(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._createFleet()
        self.bg = pygame.image.load("images/bg.bmp")

    def runGame(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    self.handleKeyDownEvents(event)
                if event.type == pygame.KEYUP:
                    self.handleKeyUpEvents(event)
            #self.screen.fill(self.settings.backgroundColor)
            self.screen.blit(self.bg, (0, 0))

            if self.stats.gameActive:
                self.ship.blitme()
                self.ship.moveShip(self)
                self._updateAliens()
                self._updateBullets()
                self._checkFleetEdges()

            pygame.display.flip()

    
    def handleKeyUpEvents(self,event):
        if event.key == pygame.K_UP:
            self.ship.movingUp = False
        if event.key == pygame.K_DOWN:
            self.ship.movingDown = False
    def handleKeyDownEvents(self,event):
        if event.key == pygame.K_q:
            sys.exit()
        if event.key == pygame.K_UP:
            self.ship.movingUp = True
        if event.key == pygame.K_DOWN:
            self.ship.movingDown = True
        if event.key == pygame.K_SPACE:
            self._createBullet()
        if event.key == pygame.K_0:
            self.stats.gameActive = not self.stats.gameActive

    def _createBullet(self):
        if len(self.bullets) < self.settings.allowedBulletAmount:
            newBullet = Bullet(self)
            self.bullets.add(newBullet)
    def _updateBullets(self):
        for bullet in self.bullets.sprites():
            bullet.blitme()
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.x > self.settings.screenWidth:
                self.bullets.remove(bullet)
        collisions = pygame.sprite.groupcollide(self.bullets,self.aliens,True,True)
        
    def _createFleet(self):
        alien = Alien(self)
        #self.aliens.add(alien)
        #this is row:
        #space available : (spaceShip.width + 3 * alien.width) - screen.width
        alienWidth = alien.rect.width
        spaceAvailableX = self.settings.screenWidth - (self.ship.rect.width + (3 * alienWidth))
        howManyAliensX = spaceAvailableX // (2 * alienWidth)
       # print(howManyAliensX)
        #columns:
        # space available: (2 * alien.height ) - screen.Height I think...
        spaceAvailableY = self.settings.screenHeight - (2 * alien.rect.height)
        howManyAliensY = spaceAvailableY // alien.rect.height    
        for i in range(howManyAliensY):
            for j in range(howManyAliensX):
                self._createAlien(i,j)
        
    def _createAlien(self,i,j):
        alien = Alien(self)
        alienWidth = alien.rect.width
        alienHeight = alien.rect.height
        
        alien.y = alienHeight * i + alienHeight
        alien.rect.y = alien.y
            #newAlien = Alien(self)
        alien.x = self.settings.screenWidth - (alienWidth + 2 * alienWidth * j)
        alien.rect.x = alien.x
        print("alien created at " + str(alien.x) + " and " + str(alien.y))
        self.aliens.add(alien)
        print(len(self.aliens))

    def _createAlienAtSpecificPoint(self,x,y):
        alien = Alien(self)
        alien.rect.y = y
        alien.rect.x = x
        self.aliens.add(alien)

    def _checkFleetEdges(self):
        for alien in self.aliens.sprites():
            if(alien.checkEdges()):
                self._changeFleetDirection()
                break

    def _changeFleetDirection(self):
        for alien in self.aliens.sprites():
            alien.rect.x += self.settings.alienDropSpeed
        self.settings.alienMovementDirection *= -1

    def _updateAliens(self):
        self.aliens.update(self)
        self.aliens.draw(self.screen)
        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            self._shipHit()
        for alien in self.aliens.sprites():
            if alien.rect.x <= 0:
                print("test")

    def _shipHit(self):
        # runs when alien hits ship
        if self.stats.shipsLeft > 0:
            self.stats.shipsLeft -= 1
            print(self.stats.shipsLeft)

            #get rid of aliens and bullets
            self.bullets.empty()
            self.aliens.empty()

            #create new fleet
            self._createFleet()
            self.ship.centerShip()

            sleep(0.5)
        else:
            self.stats.gameActive = False
    
if __name__ == '__main__':
    ai = alienInvasionSideways()
    ai.runGame()
