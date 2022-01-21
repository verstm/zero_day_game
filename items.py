import pygame as pg
import random
class dagger_1:
    def __init__(self, x, y):
        self.sprite = pg.sprite.Sprite()
        self.sprite.image = pg.image.load("Assets/Sprites/objects/weapons/dagger-1.png")
        self.sprite.rect = self.sprite.image.get_rect()
        self.type = 'weapon'
        self.state = 'lying'
        self.x = x
        self.y = y
        self.damage = 10
    def update(self):
        pass