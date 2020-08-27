import pygame, os

class Player(pygame.sprite.Sprite):

    def __init__(self, playerDir, WIDTH, HEIGHT):
        pygame.sprite.Sprite.__init__(self)
        self.dir = playerDir
        self.HP = 100
        self.dead = False
        self.loadImages()
        self.lastUpdated = 0
        self.image = self.shootingFrames[0]
        self.rect = self.image.get_rect()
        self.rect.center = ((WIDTH/8), (HEIGHT - (HEIGHT / 2.5)))


    def update(self):
        if(not self.dead):
            self.animate()

    def loadImages(self):
        self.shootingFrames = [pygame.image.load(os.path.join(self.dir, "player_shoot.png"))]
        self.deathFrames = [pygame.image.load(os.path.join(self.dir, "player_stagger2.png")),
                            pygame.image.load(os.path.join(self.dir, "player_death2.png"))]

    def animate(self):
        now = pygame.time.get_ticks()
        if(self.HP > 0):
            self.image = self.shootingFrames[0]
            self.lastUpdated = pygame.time.get_ticks()
        else:
            if((now - self.lastUpdated) < 220):
                self.image = self.deathFrames[0]
            else:
                self.rect.y += 30
                self.rect.x -= 15
                self.image = self.deathFrames[1]
                self.dead = True
            

    
                               
        
        
