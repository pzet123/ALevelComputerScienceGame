import pygame, os

class Background(pygame.sprite.Sprite):

    def __init__(self, backgroundDir, WIDTH, HEIGHT):
        pygame.sprite.Sprite.__init__(self)
        self.dir = backgroundDir
        self.width = WIDTH
        self.height = HEIGHT
        self.loadImages()
        self.image = self.backgroundFrame
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)


    def update(self):
        self.animate()

    def loadImages(self):
        self.backgroundFrame = pygame.transform.scale(pygame.image.load(os.path.join(self.dir, "background.png")), (self.width, self.height))
      
    def animate(self):
        pass
        
