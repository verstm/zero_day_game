import sys
import pygame
import random
from interface import *
from pygame import time
import time
import math
from attacks import *
debug = False
pygame.init()
dspl = pygame.display.Info()
height = dspl.current_h
weight = dspl.current_w
WIDTH = weight//1.1
HEIGHT = height//1.2
FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
r1=[pygame.K_DOWN,pygame.K_LEFT,pygame.K_UP,pygame.K_RIGHT,pygame.K_n,pygame.K_m]
r2=[pygame.K_s,pygame.K_a,pygame.K_w,pygame.K_d,pygame.K_e,pygame.K_q]
r3=[pygame.K_g,pygame.K_f,pygame.K_t,pygame.K_h,pygame.K_j,pygame.K_k]
allentityes = pygame.sprite.Group()
print(WIDTH,HEIGHT)
class game:
    def __init__(self):
        self.page = 0
        self.m = menu()
        self.d = Debug_Player()
        self.p_i = None
        self.debugflag = 1
    def pagemanage(self):
        if self.page == 0:
            self.page = 1
        elif self.page == 1:
            self.m.update()
        elif self.page == 99:
            if self.debugflag:
                self.mp1 = map(self.d)
                self.p_i = PlayerInterface(self.d,WIDTH, HEIGHT, screen, allentityes, self.mp1)
                print("Fight Debugging has been started!")
                self.debugflag = 0
            self.mp1.update()
            self.p_i.update()
            self.d.update()


    def startdebuggingmode(self):
        pass
    def pagetransition(self, page):
        self.page = page
class map:
    def __init__(self, player):
        self.player = player

        self.mapgroup = pygame.sprite.Group()
        self.map = pygame.sprite.Sprite()
        self.map.image = pygame.image.load("Assets/Sprites/Map_parts/background.png")
        self.map.image = pygame.transform.scale(self.map.image,(self.map.image.get_width() * 3,self.map.image.get_height() * 3))
        self.map.rect = self.map.image.get_rect()
        self.x = 0
        self.y = 0
        self.side1 = 0
        self.side2 = 0
        self.side3 = 0
        self.side4 = 0
        self.playerx = self.player.sprite.rect.x - self.map.rect.x
        self.playery = self.player.sprite.rect.y - self.map.rect.x
        self.mapzonex = 0
        self.mapzoney = 0

        self.x2 = self.player.sprite.rect.x
        self.y2 = self.player.sprite.rect.y
        self.map.rect = self.map.image.get_rect()
        self.map.rect.x = self.x
        self.map.rect.y = self.y
        self.mapgroup.add(self.map)
    def update(self):
        '''self.x = self.player.sprite.rect.x
        self.y = self.player.sprite.rect.y
        (self.mapzonex + x >= 0 and self.mapzonex + self.player.sprite.rect.width + x <= self.map.rect.width) and \
                (self.mapzoney + y >= 0 and self.mapzoney + self.player.sprite.rect.height + y <= self.map.rect.height)'''
        self.mapgroup.update()
        self.mapgroup.draw(screen)
    def mapmoving(self,x,y):
        # print(self.mapzonex + x, self.map.rect.width - WIDTH, self.mapzoney + y, self.map.rect.height  - HEIGHT)
        if self.mapzonex + x <= 0:
            self.side2 = 1
        else:
            self.side2 = 0
        if self.mapzonex + x >= self.map.rect.width - WIDTH:
            self.side4 = 1
        else:
            self.side4 = 0
        if self.mapzoney + y <= 0:
            self.side3 = 1
        else:
            self.side3 = 0
        if self.mapzoney + y >= self.map.rect.height - HEIGHT:
            self.side1 = 1
        else:
            self.side1 = 0
        if not (self.side2 or self.side4):
            self.x -= x
            self.playerx += x
            self.mapzonex += x
            self.map.rect.x = self.x
        if not (self.side1 or self.side3):
            self.y -= y
            self.playery += y
            self.mapzoney += y
            self.map.rect.y = self.y
        print(self.side1, self.side2, self.side3, self.side4)

        if self.side4 or self.side2:
            print('x')
            self.player.sprite.rect.x += x
            self.playerx += x
            self.mapzonex += x
        if self.side3 or self.side1:
            self.player.sprite.rect.y += y
            self.playery += y
            self.mapzoney += y
            print('y')
class menu:
    def __init__(self):
        self.background = pygame.sprite.Sprite()
        self.background.image = pygame.surface.Surface((WIDTH, HEIGHT))
        self.background.image.fill((0,0,100))
        self.background.rect = self.background.image.get_rect()
        self.background.rect.x = 0
        self.background.rect.y = 0
        self.btn_1 = pygame.image.load("Assets/Sprites/menu-1-1.png")
        self.btn_1_active = pygame.image.load("Assets/Sprites/menu-1-2.png")
        self.btn_1.set_colorkey((255,255,255))
        self.btn_1_active.set_colorkey((255,255,255))
        self.menu_elms = pygame.sprite.Group()
        self.button_1 = pygame.sprite.Sprite()
        self.button_1.image = self.btn_1.convert()
        self.button_1.rect = self.button_1.image.get_rect()
        self.button_1.rect.x = 200
        self.button_1.rect.y = 50

        self.menu_elms.add(self.background)
        self.menu_elms.add(self.button_1)

    def update(self):
        self.menu_elms.update()
        self.menu_elms.draw(screen)
        x, y = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button.
                    x, y = pygame.mouse.get_pos()
                    if x > self.button_1.rect.x and x < self.button_1.rect.x + self.button_1.rect.width and y > self.button_1.rect.y and y < self.button_1.rect.y + self.button_1.rect.height:
                        g.pagetransition(99)


        if x > self.button_1.rect.x and x < self.button_1.rect.x + self.button_1.rect.width and y > self.button_1.rect.y and y < self.button_1.rect.y + self.button_1.rect.height:
            if debug:
                print("button_active")
            self.button_1.image = self.btn_1_active
        else:
            self.button_1.image = self.btn_1
        if g.page != 1:
            self.menu_elms.empty()
            print('menu cleaned')
class Debug_Player:
    def __init__(self):
        self.spells = ['Fireball', 'Fireball']
        self.remote = r2
        self.dashkd = 3
        self.attacks = []
        self.dashtime = time.time()
        self.way = 0
        self.armx = 12
        self.army = -5
        self.heady = 22
        self.parts = 6
        self.legx = 6
        self.legy = 17
        self.bodyy = 7
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.speeed = 3
        self.health = 1000

        self.char_group = pygame.sprite.Group()
        self.sprite = pygame.sprite.Sprite()
        self.sprite.health = self.health
        self.sprite.image = pygame.surface.Surface((32,60)).convert()
        self.sprite.image.fill((255, 255, 255))
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.x, self.sprite.rect.y = self.x,self.y
        self.sprite.cls = self

        self.chest = pygame.sprite.Sprite()
        self.chest.health = 100
        self.chestsprite1 = pygame.image.load("Assets/Sprites/Character_parts/Body_parts/chest.png").convert()
        self.chestsprite2 = pygame.image.load("Assets/Sprites/Character_parts/Body_parts/chest_front.png").convert()
        self.left_arm = pygame.sprite.Sprite()
        self.left_arm.health = 100
        self.left_armsprite1 = pygame.image.load("Assets/Sprites/Character_parts/Body_parts/left_arm.png").convert()
        self.right_arm = pygame.sprite.Sprite()
        self.right_arm.health = 100
        self.right_armsprite1 = pygame.image.load("Assets/Sprites/Character_parts/Body_parts/right_arm.png").convert()
        self.right_armsprite2 = pygame.image.load("Assets/Sprites/Character_parts/Body_parts/right_arm_rightfront.png").convert()
        self.head = pygame.sprite.Sprite()
        self.head.health = 100
        self.headsprite1 = pygame.image.load("Assets/Sprites/Character_parts/Body_parts/head.png").convert()
        self.headsprite2 = pygame.image.load("Assets/Sprites/Character_parts/Body_parts/head_rightfront.png").convert()
        self.left_leg = pygame.sprite.Sprite()
        self.left_leg.health = 100
        self.left_legsprite1 = pygame.image.load("Assets/Sprites/Character_parts/Body_parts/left_leg.png").convert()
        self.left_legsprite2 = pygame.image.load("Assets/Sprites/Character_parts/Body_parts/left_leg_rightfront.png").convert()
        self.right_leg = pygame.sprite.Sprite()
        self.right_leg.health = 100
        self.right_legsprite1 = pygame.image.load("Assets/Sprites/Character_parts/Body_parts/right_leg.png").convert()
        self.right_legsprite2 = pygame.image.load("Assets/Sprites/Character_parts/Body_parts/right_leg_rightfront.png").convert()

        self.holdparts = []
        self.flg1 = 1
        allentityes.add(self.sprite)
        for i in self.char_group:
            self.holdparts.append(i)
    def update(self):
        self.moving = 0
        for i in self.char_group:
            if i.health <= 0:
                self.parts -= 1
                i.health = 1
        for i in self.attacks:
            i.update()
        self.char_group.update()
        self.char_group.draw(screen)
        keystate = pygame.key.get_pressed()
        if keystate[self.remote[1]]:
            g.mp1.mapmoving(-self.speeed, 0)
            self.way = 1
            self.moving = 1
        if keystate[self.remote[3]]:
            g.mp1.mapmoving(self.speeed, 0)
            self.way = 3
            self.moving = 1

        if keystate[self.remote[2]]:
            g.mp1.mapmoving(0, -self.speeed)
            self.way = 2
            self.moving = 1

        if keystate[self.remote[0]]:
            g.mp1.mapmoving(0, self.speeed)
            self.way = 0
            self.moving = 1
        if keystate[pygame.K_LALT]:
            if self.dashtime+self.dashkd < time.time():
                self.d = dash(g,self)
                self.dashtime = time.time()

            print("dash")



        self.partsholding()
    def partsholding(self):
        self.t = 2.3
        if self.way == 0:

            self.chest.image = self.chestsprite1
            self.chest.image.set_colorkey((255, 255, 255))
            self.chest.rect = self.chest.image.get_rect()
            self.chest.image = pygame.transform.scale(self.chest.image,
                                                      (self.chest.rect.width * 2, self.chest.rect.height * 2))
            self.chest.rect = self.chest.image.get_rect()
            self.chest.rect.centerx = self.sprite.rect.x + (self.sprite.rect.width // 2)
            self.chest.rect.centery = self.sprite.rect.y + (self.sprite.rect.height // 2)-self.bodyy

            self.left_arm.image = self.left_armsprite1
            self.left_arm.image.set_colorkey((255, 255, 255))
            self.left_arm.rect = self.left_arm.image.get_rect()
            self.left_arm.image = pygame.transform.scale(self.left_arm.image,
                                                         (self.left_arm.rect.width * 2, self.left_arm.rect.height * 2))
            self.left_arm.rect = self.left_arm.image.get_rect()
            self.left_arm.rect.centerx = self.sprite.rect.x + (self.sprite.rect.width // 2 + self.armx)
            self.left_arm.rect.centery = self.sprite.rect.y + (self.sprite.rect.height // 2 + self.army)

            self.right_arm.image = self.right_armsprite1
            self.right_arm.image.set_colorkey((255, 255, 255))
            self.right_arm.rect = self.right_arm.image.get_rect()
            self.right_arm.image = pygame.transform.scale(self.right_arm.image, (
            self.right_arm.rect.width * 2, self.right_arm.rect.height * 2))
            self.right_arm.rect = self.right_arm.image.get_rect()
            self.right_arm.rect.centerx = self.sprite.rect.x + (self.sprite.rect.width // 2 - self.armx)
            self.right_arm.rect.centery = self.sprite.rect.y + (self.sprite.rect.height // 2 + self.army)

            self.head.image = self.headsprite1
            self.head.image.set_colorkey((255, 255, 255))
            self.head.rect = self.head.image.get_rect()
            self.head.image = pygame.transform.scale(self.head.image,
                                                     (self.head.rect.width * 2, self.head.rect.height * 2))
            self.head.rect = self.head.image.get_rect()
            self.head.rect.centerx = self.sprite.rect.x + (self.sprite.rect.width // 2)
            self.head.rect.centery = self.sprite.rect.y + (self.sprite.rect.height // 2 - self.heady)

            self.left_leg.image = self.left_legsprite1
            self.left_leg.image.set_colorkey((255, 255, 255))
            self.left_leg.rect = self.left_leg.image.get_rect()
            self.left_leg.image = pygame.transform.scale(self.left_leg.image,
                                                         (self.left_leg.rect.width * 2, self.left_leg.rect.height * 2))
            self.left_leg.rect = self.left_leg.image.get_rect()
            self.left_leg.rect.centerx = self.sprite.rect.x + (self.sprite.rect.width // 2 + self.legx)
            self.left_leg.rect.centery = self.sprite.rect.y + (self.sprite.rect.height // 2 + self.legy)

            self.right_leg.image = self.right_legsprite1
            self.right_leg.image.set_colorkey((255, 255, 255))
            self.right_leg.rect = self.right_leg.image.get_rect()
            self.right_leg.image = pygame.transform.scale(self.right_leg.image, (
            self.right_leg.rect.width * 2, self.right_leg.rect.height * 2))
            self.right_leg.rect = self.right_leg.image.get_rect()
            self.right_leg.rect.centerx = self.sprite.rect.x + (self.sprite.rect.width // 2 - self.legx)
            self.right_leg.rect.centery = self.sprite.rect.y + (self.sprite.rect.height // 2 + self.legy)
            self.char_group.empty()
            self.char_group.add(self.sprite, self.chest, self.right_arm,self.left_arm, self.head, self.left_leg,
                                self.right_leg)
        if self.way == 3:
            self.chest.image = self.chestsprite2
            self.chest.image.set_colorkey((255, 255, 255))
            self.chest.rect = self.chest.image.get_rect()
            self.chest.image = pygame.transform.scale(self.chest.image,
                                                      (self.chest.rect.width * self.t, self.chest.rect.height * self.t))
            self.chest.rect = self.chest.image.get_rect()
            self.chest.rect.centerx = self.sprite.rect.x + (self.sprite.rect.width // 2)
            self.chest.rect.centery = self.sprite.rect.y + (self.sprite.rect.height // 2)

            self.right_arm.image = self.right_armsprite2
            self.right_arm.image.set_colorkey((0,0,0))
            self.right_arm.rect = self.right_arm.image.get_rect()
            self.right_arm.image = pygame.transform.scale(self.right_arm.image, (
                self.right_arm.rect.width * self.t, self.right_arm.rect.height * self.t))
            self.right_arm.rect = self.right_arm.image.get_rect()
            self.right_arm.rect.centerx = self.sprite.rect.x + (self.sprite.rect.width // 2)
            self.right_arm.rect.centery = self.sprite.rect.y + (self.sprite.rect.height // 2 + self.army)

            self.head.image = self.headsprite2
            self.head.image.set_colorkey((255, 255, 255))
            self.head.rect = self.head.image.get_rect()
            self.head.image = pygame.transform.scale(self.head.image,
                                                     (self.head.rect.width * self.t, self.head.rect.height * self.t))
            self.head.rect = self.head.image.get_rect()
            self.head.rect.centerx = self.sprite.rect.x + (self.sprite.rect.width // 2)
            self.head.rect.centery = self.sprite.rect.y + (self.sprite.rect.height // 2 - self.heady)+4

            self.left_leg.image = self.left_legsprite2
            self.left_leg.image.set_colorkey((255, 255, 255))
            self.left_leg.rect = self.left_leg.image.get_rect()
            self.left_leg.image = pygame.transform.scale(self.left_leg.image,
                                                         (self.left_leg.rect.width * self.t, self.left_leg.rect.height * self.t))
            self.left_leg.rect = self.left_leg.image.get_rect()
            self.left_leg.rect.centerx = self.sprite.rect.x + (self.sprite.rect.width // 2)
            self.left_leg.rect.centery = self.sprite.rect.y + (self.sprite.rect.height // 2 + self.legy)

            self.right_leg.image = self.right_legsprite2
            self.right_leg.image.set_colorkey((255, 255, 255))
            self.right_leg.rect = self.right_leg.image.get_rect()
            self.right_leg.image = pygame.transform.scale(self.right_leg.image, (
                self.right_leg.rect.width * self.t, self.right_leg.rect.height * self.t))
            self.right_leg.rect = self.right_leg.image.get_rect()
            self.right_leg.rect.centerx = self.sprite.rect.x + (self.sprite.rect.width // 2)
            self.right_leg.rect.centery = self.sprite.rect.y + (self.sprite.rect.height // 2 + self.legy)
            self.char_group.empty()
            self.char_group.add(self.sprite, self.chest, self.right_arm, self.head, self.left_leg,
                                self.right_leg)
        if self.way == 1:
            self.chest.image = self.chestsprite2
            self.chest.image.set_colorkey((255, 255, 255))
            self.chest.rect = self.chest.image.get_rect()
            self.chest.image = pygame.transform.scale(self.chest.image,
                                                      (self.chest.rect.width * self.t, self.chest.rect.height * self.t))
            self.chest.rect = self.chest.image.get_rect()
            self.chest.rect.centerx = self.sprite.rect.x + (self.sprite.rect.width // 2)
            self.chest.rect.centery = self.sprite.rect.y + (self.sprite.rect.height // 2)

            self.left_arm.image = self.right_armsprite2
            self.left_arm.image.set_colorkey((0, 0, 0))
            self.left_arm.rect = self.left_arm.image.get_rect()
            self.left_arm.image = pygame.transform.scale(self.left_arm.image, (
                self.left_arm.rect.width * self.t, self.left_arm.rect.height * self.t))
            self.left_arm.image = pygame.transform.flip(self.left_arm.image, True, False)
            self.left_arm.rect = self.left_arm.image.get_rect()
            self.left_arm.rect.centerx = self.sprite.rect.x + (self.sprite.rect.width // 2)
            self.left_arm.rect.centery = self.sprite.rect.y + (self.sprite.rect.height // 2 + self.army)

            self.head.image = self.headsprite2
            self.head.image.set_colorkey((255, 255, 255))
            self.head.rect = self.head.image.get_rect()
            self.head.image = pygame.transform.scale(self.head.image,
                                                     (self.head.rect.width * self.t, self.head.rect.height * self.t))
            self.head.image = pygame.transform.flip(self.head.image, True, False)
            self.head.rect = self.head.image.get_rect()
            self.head.rect.centerx = self.sprite.rect.x + (self.sprite.rect.width // 2)
            self.head.rect.centery = self.sprite.rect.y + (self.sprite.rect.height // 2 - self.heady) + 4

            self.left_leg.image = self.left_legsprite2
            self.left_leg.image.set_colorkey((255, 255, 255))
            self.left_leg.rect = self.left_leg.image.get_rect()
            self.left_leg.image = pygame.transform.scale(self.left_leg.image,
                                                         (self.left_leg.rect.width * self.t, self.left_leg.rect.height * self.t))
            self.left_leg.image = pygame.transform.flip(self.left_leg.image, True, False)

            self.left_leg.rect = self.left_leg.image.get_rect()
            self.left_leg.rect.centerx = self.sprite.rect.x + (self.sprite.rect.width // 2)
            self.left_leg.rect.centery = self.sprite.rect.y + (self.sprite.rect.height // 2 + self.legy)

            self.right_leg.image = self.right_legsprite2
            self.right_leg.image.set_colorkey((255, 255, 255))
            self.right_leg.rect = self.right_leg.image.get_rect()
            self.right_leg.image = pygame.transform.scale(self.right_leg.image, (
                self.right_leg.rect.width * self.t, self.right_leg.rect.height * self.t))
            self.right_leg.image = pygame.transform.flip(self.right_leg.image, True, False)
            self.right_leg.rect = self.right_leg.image.get_rect()
            self.right_leg.rect.centerx = self.sprite.rect.x + (self.sprite.rect.width // 2)
            self.right_leg.rect.centery = self.sprite.rect.y + (self.sprite.rect.height // 2 + self.legy)
            self.char_group.empty()
            self.char_group.add(self.sprite, self.chest, self.left_arm, self.head, self.left_leg,
                                self.right_leg)
        if self.way == 2:
            self.chest.image = self.chestsprite1
            self.chest.image.set_colorkey((255, 255, 255))
            self.chest.rect = self.chest.image.get_rect()
            self.chest.image = pygame.transform.scale(self.chest.image,
            (self.chest.rect.width * 2, self.chest.rect.height * 2))
            self.chest.rect = self.chest.image.get_rect()
            self.chest.rect.centerx = self.sprite.rect.x + (self.sprite.rect.width // 2)
            self.chest.rect.centery = self.sprite.rect.y + (self.sprite.rect.height // 2) - self.bodyy

            self.left_arm.image = self.left_armsprite1
            self.left_arm.image.set_colorkey((255, 255, 255))
            self.left_arm.rect = self.left_arm.image.get_rect()
            self.left_arm.image = pygame.transform.scale(self.left_arm.image,
                                                         (self.left_arm.rect.width * 2, self.left_arm.rect.height * 2))
            self.left_arm.rect = self.left_arm.image.get_rect()
            self.left_arm.rect.centerx = self.sprite.rect.x + (self.sprite.rect.width // 2 + self.armx)
            self.left_arm.rect.centery = self.sprite.rect.y + (self.sprite.rect.height // 2 + self.army)

            self.right_arm.image = self.right_armsprite1
            self.right_arm.image.set_colorkey((255, 255, 255))
            self.right_arm.rect = self.right_arm.image.get_rect()
            self.right_arm.image = pygame.transform.scale(self.right_arm.image, (
                self.right_arm.rect.width * 2, self.right_arm.rect.height * 2))
            self.right_arm.rect = self.right_arm.image.get_rect()
            self.right_arm.rect.centerx = self.sprite.rect.x + (self.sprite.rect.width // 2 - self.armx)
            self.right_arm.rect.centery = self.sprite.rect.y + (self.sprite.rect.height // 2 + self.army)

            self.head.image = self.headsprite1
            self.head.image.set_colorkey((255, 255, 255))
            self.head.rect = self.head.image.get_rect()
            self.head.image = pygame.transform.scale(self.head.image,
                                                     (self.head.rect.width * 2, self.head.rect.height * 2))
            self.head.rect = self.head.image.get_rect()
            self.head.rect.centerx = self.sprite.rect.x + (self.sprite.rect.width // 2)
            self.head.rect.centery = self.sprite.rect.y + (self.sprite.rect.height // 2 - self.heady)

            self.left_leg.image = self.left_legsprite1
            self.left_leg.image.set_colorkey((255, 255, 255))
            self.left_leg.rect = self.left_leg.image.get_rect()
            self.left_leg.image = pygame.transform.scale(self.left_leg.image,
                                                         (self.left_leg.rect.width * 2, self.left_leg.rect.height * 2))
            self.left_leg.rect = self.left_leg.image.get_rect()
            self.left_leg.rect.centerx = self.sprite.rect.x + (self.sprite.rect.width // 2 + self.legx)
            self.left_leg.rect.centery = self.sprite.rect.y + (self.sprite.rect.height // 2 + self.legy)

            self.right_leg.image = self.right_legsprite1
            self.right_leg.image.set_colorkey((255, 255, 255))
            self.right_leg.rect = self.right_leg.image.get_rect()
            self.right_leg.image = pygame.transform.scale(self.right_leg.image, (
                self.right_leg.rect.width * 2, self.right_leg.rect.height * 2))
            self.right_leg.rect = self.right_leg.image.get_rect()
            self.right_leg.rect.centerx = self.sprite.rect.x + (self.sprite.rect.width // 2 - self.legx)
            self.right_leg.rect.centery = self.sprite.rect.y + (self.sprite.rect.height // 2 + self.legy)
            self.char_group.empty()
            self.char_group.add(self.sprite, self.chest, self.right_arm, self.left_arm, self.head, self.left_leg,self.right_leg)
    def on_click(self, button):
        pass
    def getdamage(self, damage, type, *args):
        damage = damage
        y = 0
        for i in self.char_group:
            if i != self.sprite:
                y += 1
                print(len(self.char_group))
                x = random.randint(2,10)
                if y != self.parts:
                    i.health -= damage // x
                    damage -= damage // x
                else:
                    i.health -= damage
    def spritemove(self, x,y):
        g.mp1.mapmoving(x,y)
class chat:
    def __init__(self, x, y):
        pass
class itemstech:
    def __init__(self):
        self.itemsgroup = pygame.sprite.Group()
        self.allitems = []
        self.itemsinvis = []
    def update(self):
        for i in range(len(self.allitems)):
            if self.allitems[i][1] >= -10:
                print('xd')
        self.itemsgroup.empty()
        for i in range(len(self.itemsinvis)):
            self.itemsgroup.add(self.itemsinvis[i])
        self.itemsgroup.update()
        self.itemsgroup.draw(screen)
    def itemspawn(self, item, x, y, *args):
        self.allitems.append([item,x,y])
g = game()
clock = pygame.time.Clock()
while True:
    screen.fill((0,0,0))
    screen.fill((255, 255, 255))
    g.pagemanage()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    clock.tick(FPS)
    pygame.display.update()
    pygame.display.flip()