import pygame
import time
import math
class explosion:
    def __init__(self, rad, pow,x,y,sc, allnt, map):
        self.power = pow
        self.screen = sc
        self.allentityes = allnt
        self.radius = rad
        self.x = x
        self.y = y
        self.map = map
        self.x2 = x
        self.y2 = y
        self.flg = 1
        self.x3 = self.map.playerx
        self.y3 = self.map.playery
        self.anim = 1
        self.sprite = pygame.image.load("Assets/Sprites/Effects/explosion/"+str(self.anim)+".png")
        '''     self.sprite = pygame.Surface((self.radius,self.radius))
                self.sprite.fill((255,255,255))
                x = pygame.draw.circle(self.sprite,(255,128,0),(self.radius//2,self.radius//2),self.radius//2,9999)
                self.sprite.set_colorkey((255,255,255))'''
        self.expsprite = pygame.sprite.Sprite()
        self.expsprite.image = pygame.image.load("Assets/Sprites/Effects/explosion/"+str(self.anim)+".png")
        self.expsprite.rect = self.expsprite.image.get_rect()
        self.expsprite.rect.centerx = self.x
        self.expsprite.rect.centery = self.y
        self.expgroup = pygame.sprite.Group()
        self.expgroup.add(self.expsprite)
        self.timer = 0
        self.livetime = 16
        self.living = 1
    def update(self):
        self.expsprite.image = pygame.image.load("Assets/Sprites/Effects/explosion/"+str(self.anim)+".png")
        self.expsprite.image.set_colorkey((255,255,255))
        self.x = self.x2 - (self.map.playerx - self.x3)
        self.y = self.y2 - (self.map.playery - self.y3)
        self.expsprite.rect.centerx = self.x
        self.expsprite.rect.centery = self.y
        if self.timer <= self.livetime:
            if self.timer // 2 > self.anim:
                self.anim += 1
            self.collides = pygame.sprite.spritecollide(self.expsprite, self.allentityes, False)
            if self.flg:
                for i in self.collides:
                    n = pygame.math.Vector2(i.rect.x, i.rect.y) - self.expsprite.rect.center
                    d = abs(n[0])+abs(n[1])
                    i.cls.getdamage(((self.radius - d) * self.power) // 5, 'explosion')
                self.flg = 0
            self.timer += 1

            self.expgroup.update()
            self.expgroup.draw(self.screen)

        else:
            self.expgroup.empty()
            self.expsprite.kill()
            self.living = 0