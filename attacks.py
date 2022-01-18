import pygame
import time
import math
from Harm_events import *
class fireball:
    def __init__(self, cls, sc, allnt):
        self.screen = sc
        self.allnt = allnt
        self.balldir = "Assets\Sprites\Attacks\Fireball"
        self.ballanim_dir = "Assets\Sprites\Attacks\Fireball\Animation"
        self.ballsprite = None
        self.player = cls
        self.scatt = 30
        self.tscatt = 10
        self.state = 0
        self.targetx = None
        self.targety = None
        self.animstate = 1
        self.ballgroup = pygame.sprite.Group()
        self.flg1 = 1
        self.flg2 = 1
        self.living = 1
    def move(self, x,y,speed):
        try:
            # Find direction vector (dx, dy) between enemy and player.
            dx, dy = x - self.ball.rect.x, y - self.ball.rect.y
            dist = math.hypot(dx, dy)
            dx, dy = dx / dist, dy / dist  # Normalize.
            # Move along this normalized vector towards the player at current speed.
            self.ball.rect.x += dx * speed
            self.ball.rect.y += dy * speed
        except:
            pass

    def point_at(self,x,y):
        self.img_orig = pygame.image.load(self.ballsprite)
        self.direction = pygame.math.Vector2(x, y) - self.ball.rect.center
        if self.direction.length() > 0:
            self.direction = self.direction.normalize()
        angle = self.direction.angle_to((0, 0)) + 180
        self.ball.image = pygame.transform.rotate(self.img_orig, angle)
        self.ball.rect = self.ball.image.get_rect(center=self.ball.rect.center)
    def update(self):
        if self.state == 0:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.targetx, self.targety = pygame.mouse.get_pos()
                        self.state += 1
        elif self.state == 1:
            self.ballsprite = self.ballanim_dir + "\\" + str(self.animstate) + '.png'
            if self.flg1:
                self.ball = pygame.sprite.Sprite()
                self.ball.image = pygame.image.load(self.ballsprite)
                self.ball.rect = self.ball.image.get_rect()
                self.ball.rect.x = self.player.sprite.rect.x
                self.ball.rect.y = self.player.sprite.rect.y + 30
                self.ballgroup.add(self.ball)
                self.flg1 = 0
            self.ball.image = pygame.image.load(self.ballsprite)
            self.ball.image.set_colorkey((22,22,22))

            if (self.targetx >= self.ball.rect.x - self.scatt and self.targetx <= self.ball.rect.x + self.scatt) and (self.targety >= self.ball.rect.y - self.scatt and self.targety <= self.ball.rect.y + self.scatt):
                self.state += 1
                self.ball.kill()
            else:
                self.point_at(self.targetx, self.targety)
                self.move(self.targetx,self.targety,30)

            self.animstate += 1
            if self.animstate > 9:
                self.animstate = 1
            self.ballgroup.update()
            self.ballgroup.draw(self.screen)
        elif self.state == 2:
            if self.flg2:
                self.e = explosion(200, 5, self.targetx, self.targety, self.screen, self.allnt)
                self.flg2 = 0
            if self.e.living:
                self.e.update()
            else:
                del self.e
                self.state += 1
        else:
            self.living = 0