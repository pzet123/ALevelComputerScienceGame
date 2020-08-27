import pygame, sys, os, time, random
from pygame.locals import *
from player import Player
from enemy import Enemy
from background import Background

pygame.init()

WINDOW_SIZE = (1280, 720)
window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Interactive study")

currentDir = os.getcwd()
assetsDir = os.path.join(currentDir, "Assets")
enemyDir = (os.path.join(assetsDir, "Enemy"))
backgroundDir = (os.path.join(assetsDir, "Background"))
eliminationDir = (os.path.join(assetsDir, "Elimination"))
playerDir = (os.path.join(assetsDir, "Player"))


allSprites = pygame.sprite.Group()

cloudImg = pygame.image.load(os.path.join(backgroundDir, "cloud.png")).convert_alpha()

WHITE = (255, 255, 255)
clock = pygame.time.Clock()
FPS = 30


running = True

player1 = Player(playerDir, WINDOW_SIZE[0], WINDOW_SIZE[1])
enemy1 = Enemy(enemyDir, WINDOW_SIZE[0], WINDOW_SIZE[1])
background = Background(backgroundDir, WINDOW_SIZE[0], WINDOW_SIZE[1])
allSprites.add(background)
allSprites.add(player1)
allSprites.add(enemy1)

def detectEvents():
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

count = 0
def drawGameWindow():
    clock.tick(FPS)
    window.fill(WHITE)
    allSprites.update()
    allSprites.draw(window)
    pygame.display.update()

while(running):

    detectEvents()
    drawGameWindow()



