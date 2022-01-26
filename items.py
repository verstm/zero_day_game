import pygame as pg
import random
class dagger_1:
    def __init__(self, x, y, map):
        self.map = map
        self.sprite = pg.sprite.Sprite()
        self.sprite.image = pg.image.load("Assets/Sprites/objects/weapons/dagger-1.png")
        self.sprite.rect = self.sprite.image.get_rect()
        self.player = self.map.player
        self.sprite.image = pg.transform.scale(self.sprite.image,
                                                  (self.sprite.rect.width * 2, self.sprite.rect.height * 2))
        self.sprite.rect = self.sprite.image.get_rect()
        self.type = 'weapon'
        self.state = 'lying'
        self.x = x
        self.y = y
        self.damage = 10
    def update(self):
        self.sprite.rect.x = self.x + self.map.x
        self.sprite.rect.y = self.y + self.map.y
        self.interactioncheck()
    def interactioncheck(self):
        for i in pg.event.get():
            if i.type == pg.MOUSEBUTTONDOWN:
                if i.button == 1:
                    x, y = pg.mouse.get_pos()
                    if (x >= self.sprite.rect.x and x <= self.sprite.rect.x + self.sprite.rect.width) and \
                        (y >= self.sprite.rect.y and y <= self.sprite.rect.y + self.sprite.rect.height):
                        self.onclick()
    def onclick(self):
        n = pg.math.Vector2(self.player.sprite.rect.x, self.player.sprite.rect.y) - self.sprite.rect.center
        d = abs(n[0]) + abs(n[1])
        print(d)
# xd3
