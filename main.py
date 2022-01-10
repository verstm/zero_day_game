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
                self.p_i = PlayerInterface(self.d,WIDTH, HEIGHT, screen)
                print("Fight Debugging has been started!")
                self.debugflag = 0
            self.p_i.update()
            self.d.update()


    def startdebuggingmode(self):
        pass
    def pagetransition(self, page):
        self.page = page
class map:
    def __init__(self):
        self.mapgroup = pygame.sprite.Group()
        self.map = pygame.sprite.Sprite()
        self.map.image = pygame.image.load("Assets/Sprites/Map_parts/background.png")
        self.map.rect = self.map.image.get_rect()
        self.x = 0
        self.y = 0
    def update(self):
        self.map.rect.x = self.x
        self.map.rect.y = self.y
    def mapmoving(self,x,y):
        self.x += x
        self.y += y
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
        self.spells = ['Fireball']
        self.remote = r2
        self.attacks = []
        self.way = 0
        self.armx = 12
        self.army = -5
        self.heady = 22
        self.legx = 6
        self.legy = 17
        self.bodyy = 7
        self.x = 100
        self.y = 100
        self.speeed = 2

        self.char_group = pygame.sprite.Group()
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = pygame.surface.Surface((32,60)).convert()
        self.sprite.image.fill((255, 255, 255))
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.x, self.sprite.rect.y = self.x,self.y

        self.chest = pygame.sprite.Sprite()
        self.chestsprite1 = pygame.image.load("Assets/Sprites/Character_parts/Body_parts/chest.png").convert()
        self.chestsprite2 = pygame.image.load("Assets/Sprites/Character_parts/Body_parts/chest_front.png").convert()
        self.left_arm = pygame.sprite.Sprite()
        self.left_armsprite1 = pygame.image.load("Assets/Sprites/Character_parts/Body_parts/left_arm.png").convert()
        self.right_arm = pygame.sprite.Sprite()
        self.right_armsprite1 = pygame.image.load("Assets/Sprites/Character_parts/Body_parts/right_arm.png").convert()
        self.right_armsprite2 = pygame.image.load("Assets/Sprites/Character_parts/Body_parts/right_arm_rightfront.png").convert()
        self.head = pygame.sprite.Sprite()
        self.headsprite1 = pygame.image.load("Assets/Sprites/Character_parts/Body_parts/head.png").convert()
        self.headsprite2 = pygame.image.load("Assets/Sprites/Character_parts/Body_parts/head_rightfront.png").convert()
        self.left_leg = pygame.sprite.Sprite()
        self.left_legsprite1 = pygame.image.load("Assets/Sprites/Character_parts/Body_parts/left_leg.png").convert()
        self.left_legsprite2 = pygame.image.load("Assets/Sprites/Character_parts/Body_parts/left_leg_rightfront.png").convert()
        self.right_leg = pygame.sprite.Sprite()
        self.right_legsprite1 = pygame.image.load("Assets/Sprites/Character_parts/Body_parts/right_leg.png").convert()
        self.right_legsprite2 = pygame.image.load("Assets/Sprites/Character_parts/Body_parts/right_leg_rightfront.png").convert()

        self.holdparts = []
        self.flg1 = 1
        for i in self.char_group:
            self.holdparts.append(i)
    def update(self):
        for i in self.attacks:
            i.update()
        self.char_group.update()
        self.char_group.draw(screen)
        keystate = pygame.key.get_pressed()
        if keystate[self.remote[1]]:
            self.sprite.rect.x -= self.speeed
            self.way = 1
            self.moving = 1
        if keystate[self.remote[3]]:
            self.sprite.rect.x += self.speeed
            self.way = 3
            self.moving = 1

        if keystate[self.remote[2]]:
            self.sprite.rect.y -= self.speeed
            self.way = 2
            self.moving = 1

        if keystate[self.remote[0]]:
            self.sprite.rect.y += self.speeed
            self.way = 0
            self.moving = 1



        self.partsholding()
    def partsholding(self):
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
                                                      (self.chest.rect.width * 2, self.chest.rect.height * 2))
            self.chest.rect = self.chest.image.get_rect()
            self.chest.rect.centerx = self.sprite.rect.x + (self.sprite.rect.width // 2)
            self.chest.rect.centery = self.sprite.rect.y + (self.sprite.rect.height // 2)

            self.right_arm.image = self.right_armsprite2
            self.right_arm.image.set_colorkey((0,0,0))
            self.right_arm.rect = self.right_arm.image.get_rect()
            self.right_arm.image = pygame.transform.scale(self.right_arm.image, (
                self.right_arm.rect.width * 2, self.right_arm.rect.height * 2))
            self.right_arm.rect = self.right_arm.image.get_rect()
            self.right_arm.rect.centerx = self.sprite.rect.x + (self.sprite.rect.width // 2)
            self.right_arm.rect.centery = self.sprite.rect.y + (self.sprite.rect.height // 2 + self.army)

            self.head.image = self.headsprite2
            self.head.image.set_colorkey((255, 255, 255))
            self.head.rect = self.head.image.get_rect()
            self.head.image = pygame.transform.scale(self.head.image,
                                                     (self.head.rect.width * 2, self.head.rect.height * 2))
            self.head.rect = self.head.image.get_rect()
            self.head.rect.centerx = self.sprite.rect.x + (self.sprite.rect.width // 2)
            self.head.rect.centery = self.sprite.rect.y + (self.sprite.rect.height // 2 - self.heady)+4

            self.left_leg.image = self.left_legsprite2
            self.left_leg.image.set_colorkey((255, 255, 255))
            self.left_leg.rect = self.left_leg.image.get_rect()
            self.left_leg.image = pygame.transform.scale(self.left_leg.image,
                                                         (self.left_leg.rect.width * 2, self.left_leg.rect.height * 2))
            self.left_leg.rect = self.left_leg.image.get_rect()
            self.left_leg.rect.centerx = self.sprite.rect.x + (self.sprite.rect.width // 2)
            self.left_leg.rect.centery = self.sprite.rect.y + (self.sprite.rect.height // 2 + self.legy)

            self.right_leg.image = self.right_legsprite2
            self.right_leg.image.set_colorkey((255, 255, 255))
            self.right_leg.rect = self.right_leg.image.get_rect()
            self.right_leg.image = pygame.transform.scale(self.right_leg.image, (
                self.right_leg.rect.width * 2, self.right_leg.rect.height * 2))
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
                                                      (self.chest.rect.width * 2, self.chest.rect.height * 2))
            self.chest.rect = self.chest.image.get_rect()
            self.chest.rect.centerx = self.sprite.rect.x + (self.sprite.rect.width // 2)
            self.chest.rect.centery = self.sprite.rect.y + (self.sprite.rect.height // 2)

            self.left_arm.image = self.right_armsprite2
            self.left_arm.image.set_colorkey((0, 0, 0))
            self.left_arm.rect = self.left_arm.image.get_rect()
            self.left_arm.image = pygame.transform.scale(self.left_arm.image, (
                self.left_arm.rect.width * 2, self.left_arm.rect.height * 2))
            self.left_arm.image = pygame.transform.flip(self.left_arm.image, True, False)
            self.left_arm.rect = self.left_arm.image.get_rect()
            self.left_arm.rect.centerx = self.sprite.rect.x + (self.sprite.rect.width // 2)
            self.left_arm.rect.centery = self.sprite.rect.y + (self.sprite.rect.height // 2 + self.army)

            self.head.image = self.headsprite2
            self.head.image.set_colorkey((255, 255, 255))
            self.head.rect = self.head.image.get_rect()
            self.head.image = pygame.transform.scale(self.head.image,
                                                     (self.head.rect.width * 2, self.head.rect.height * 2))
            self.head.image = pygame.transform.flip(self.head.image, True, False)
            self.head.rect = self.head.image.get_rect()
            self.head.rect.centerx = self.sprite.rect.x + (self.sprite.rect.width // 2)
            self.head.rect.centery = self.sprite.rect.y + (self.sprite.rect.height // 2 - self.heady) + 4

            self.left_leg.image = self.left_legsprite2
            self.left_leg.image.set_colorkey((255, 255, 255))
            self.left_leg.rect = self.left_leg.image.get_rect()
            self.left_leg.image = pygame.transform.scale(self.left_leg.image,
                                                         (self.left_leg.rect.width * 2, self.left_leg.rect.height * 2))
            self.left_leg.image = pygame.transform.flip(self.left_leg.image, True, False)

            self.left_leg.rect = self.left_leg.image.get_rect()
            self.left_leg.rect.centerx = self.sprite.rect.x + (self.sprite.rect.width // 2)
            self.left_leg.rect.centery = self.sprite.rect.y + (self.sprite.rect.height // 2 + self.legy)

            self.right_leg.image = self.right_legsprite2
            self.right_leg.image.set_colorkey((255, 255, 255))
            self.right_leg.rect = self.right_leg.image.get_rect()
            self.right_leg.image = pygame.transform.scale(self.right_leg.image, (
                self.right_leg.rect.width * 2, self.right_leg.rect.height * 2))
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