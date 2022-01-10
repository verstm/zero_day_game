import pygame
import time
import math
class explosion:
    def __init__(self, rad, pow,x,y,sc):
        self.power = pow
        self.screen = sc
        self.radius = rad
        self.x = x
        self.y = y
        self.sprite = pygame.Surface((self.radius,self.radius))
        self.sprite.fill((255,255,255))
        x = pygame.draw.circle(self.sprite,(255,128,0),(self.radius//2,self.radius//2),self.radius//2,9999)
        self.sprite.set_colorkey((255,255,255))
        self.expsprite = pygame.sprite.Sprite()
        self.expsprite.image = self.sprite
        self.expsprite.rect = self.expsprite.image.get_rect()
        self.expsprite.rect.centerx = self.x
        self.expsprite.rect.centery = self.y
        self.expgroup = pygame.sprite.Group()
        self.expgroup.add(self.expsprite)
        self.timer = 0
        self.livetime = 15
        self.living = 1
    def update(self):
        if self.timer <= self.livetime:
            self.timer += 1
            self.expgroup.update()
            self.expgroup.draw(self.screen)
        else:
            self.expgroup.empty()
            self.expsprite.kill()
            self.living = 0