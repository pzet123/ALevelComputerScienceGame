import pygame, os


#self.kill() removes a sprite from a sprite group

class Enemy(pygame.sprite.Sprite):

    def __init__(self, enemyDir, WIDTH, HEIGHT):
        pygame.sprite.Sprite.__init__(self)
        self.dir = enemyDir
        self.width = WIDTH
        self.HP = 100
        self.dead = False
        self.walking = True
        self.attacking = False
        self.loadImages()
        self.lastUpdated = 0
        self.currentWalkFrame = 0
        self.currentDeathFrame = 0
        self.image = self.walkingFrames[0]
        self.rect = self.image.get_rect()
        self.rect.center = ((WIDTH + (WIDTH/12)), (HEIGHT - (HEIGHT / 2.5)))


    def update(self):
        if(self.rect.left <= (self.width/8)):
            self.attacking = True
            self.walking = False 
        if(not self.dead):
            if(self.walking):
                self.rect.x -= 1
            self.animate()

    def loadImages(self):
        self.walkingFrames = [pygame.transform.flip(pygame.image.load(os.path.join(self.dir, "enemy_walk0.png")), True, False),
                              pygame.transform.flip(pygame.image.load(os.path.join(self.dir, "enemy_walk1.png")), True, False),
                              pygame.transform.flip(pygame.image.load(os.path.join(self.dir, "enemy_walk2.png")), True, False),
                              pygame.transform.flip(pygame.image.load(os.path.join(self.dir, "enemy_walk3.png")), True, False),
                              pygame.transform.flip(pygame.image.load(os.path.join(self.dir, "enemy_walk4.png")), True, False),
                              pygame.transform.flip(pygame.image.load(os.path.join(self.dir, "enemy_walk5.png")), True, False),
                              pygame.transform.flip(pygame.image.load(os.path.join(self.dir, "enemy_walk6.png")), True, False),
                              pygame.transform.flip(pygame.image.load(os.path.join(self.dir, "enemy_walk7.png")), True, False)]
        self.deathFrames = [pygame.image.load(os.path.join(self.dir, "enemy_die0.png")),
                            pygame.image.load(os.path.join(self.dir, "enemy_die1.png")),
                            pygame.image.load(os.path.join(self.dir, "enemy_die2.png")),
                            pygame.image.load(os.path.join(self.dir, "enemy_die3.png")),]
        self.attackFrames = [pygame.transform.flip(pygame.image.load(os.path.join(self.dir, "enemy_attack0.png")), True, False),
                             pygame.transform.flip(pygame.image.load(os.path.join(self.dir, "enemy_attack1.png")), True, False),
                             pygame.transform.flip(pygame.image.load(os.path.join(self.dir, "enemy_attack2.png")), True, False)]

    def animate(self):
        now = pygame.time.get_ticks()
        if(self.walking):
            if((now - self.lastUpdated) > 150):
                self.lastUpdated = now
                self.currentWalkFrame = ((self.currentWalkFrame + 1)% len(self.walkingFrames))
                self.image = self.walkingFrames[self.currentWalkFrame]

        if(self.HP <= 0):
            self.walking = False
            if(self.currentDeathFrame >= len(self.deathFrames) - 1):
                self.dead = True
                self.kill()
            elif((now - self.lastUpdated) > 200):
                self.rect.y += 10
                self.lastUpdated = now
                self.currentDeathFrame = (self.currentDeathFrame + 1)
                self.image = self.deathFrames[self.currentDeathFrame]
                
            
            
            
        

            
