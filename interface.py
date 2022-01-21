import pygame
from PIL import Image
from attacks import *
class PlayerInterface:
    def __init__(self, playercls, w, h, sc, allent, map):
        self.screen = sc
        self.width = w
        self.allent = allent
        self.map = map
        self.doll_group = pygame.sprite.Group()
        self.height = h
        self.player = playercls
        self.armx = 12
        self.army = -5
        self.heady = 22
        self.legx = 6
        self.legy = 17
        self.bodyy = 7
        self.dollcords = [w - 80, h - 80]
        self.interfacesprites = pygame.sprite.Group()
        self.fastslotsrpite = pygame.image.load("Assets/Sprites/Interfaces/Player_interface/cell-1.png")
        self.rightarmslot_sprite = pygame.image.load("Assets/Sprites/Interfaces/Player_interface/left_arm_slot.png")
        self.rightarmslot_active_sprite = pygame.image.load("Assets/Sprites/Interfaces/Player_interface/left_arm_slot_active.png")
        self.leftarmslot_sprite = pygame.image.load("Assets/Sprites/Interfaces/Player_interface/right_arm_slot.png")
        self.leftarmslot_active_sprite = pygame.image.load("Assets/Sprites/Interfaces/Player_interface/right_arm_slot_active.png")
        self.selectedarmslot = None

        self.rightarmslot = pygame.sprite.Sprite()
        self.rightarmslot.image = self.rightarmslot_sprite
        self.rightarmslot.rect = self.rightarmslot.image.get_rect()
        self.rightarmslot.rect.x = 100
        self.rightarmslot.rect.y = self.height - 100

        self.leftarmslot = pygame.sprite.Sprite()
        self.leftarmslot.image = self.leftarmslot_sprite
        self.leftarmslot.rect = self.leftarmslot.image.get_rect()
        self.leftarmslot.rect.x = 180
        self.leftarmslot.rect.y = self.height - 100

        self.interfacesprites.add(self.leftarmslot, self.rightarmslot)
        self.spellgroup = pygame.sprite.Group()
        self.spells = []
        self.spellicons()
    def update(self):
        self.characterdoll()
        self.spellcheck()
        self.spellgroup.empty()
        for i in self.spells:
            self.spellgroup.add(i)
        self.spellgroup.update()
        self.spellgroup.draw(self.screen)
        self.interfacesprites.update()
        self.interfacesprites.draw(self.screen)
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_1]:
            self.selectedarmslot = 1
            self.leftarmslot.image = self.leftarmslot_sprite
            self.rightarmslot.image = self.rightarmslot_active_sprite
        if keystate[pygame.K_2]:
            self.selectedarmslot = 2
            self.leftarmslot.image = self.leftarmslot_active_sprite
            self.rightarmslot.image = self.rightarmslot_sprite
    def spellicons(self):
        for i in self.player.spells:
            self.spell = pygame.sprite.Sprite()
            self.spell.name = i
            self.spell.image = pygame.image.load("Assets/Sprites/Attacks/"+i+"/Icon/"+i+".png")
            self.spell.rect = self.spell.image.get_rect()
            self.spell.image = pygame.transform.scale(self.spell.image,
                                                     (self.spell.rect.width * 1.5, self.spell.rect.height * 1.5))
            self.spell.rect = self.spell.image.get_rect()
            self.spell.rect.x = 50*len(self.spells)
            self.spell.rect.y = 5
            self.spells.append(self.spell)
    def spellcheck(self):
        x,y = pygame.mouse.get_pos()
        for i in self.spells:
            if x > i.rect.x and x < i.rect.x + i.rect.width and y > i.rect.y and y < i.rect.y + i.rect.height:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            self.att = fireball(self.player, self.screen, self.allent, self.map)
                            self.player.attacks.append(self.att)
    def characterdoll(self):
        self.chest = pygame.sprite.Sprite()
        self.chestsprite1 = pygame.image.load("Assets/Sprites/Character_parts/Body_parts/chest.png").convert()
        self.left_arm = pygame.sprite.Sprite()
        self.left_armsprite1 = pygame.image.load("Assets/Sprites/Character_parts/Body_parts/left_arm.png").convert()
        self.right_arm = pygame.sprite.Sprite()
        self.right_armsprite1 = pygame.image.load("Assets/Sprites/Character_parts/Body_parts/right_arm.png").convert()
        self.head = pygame.sprite.Sprite()
        self.headsprite1 = pygame.image.load("Assets/Sprites/Character_parts/Body_parts/head.png").convert()
        self.left_leg = pygame.sprite.Sprite()
        self.left_legsprite1 = pygame.image.load("Assets/Sprites/Character_parts/Body_parts/left_leg.png").convert()
        self.right_leg = pygame.sprite.Sprite()
        self.right_legsprite1 = pygame.image.load("Assets/Sprites/Character_parts/Body_parts/right_leg.png").convert()
        self.chest.image = self.chestsprite1
        self.chest.image.set_colorkey((255, 255, 255))
        self.chest.rect = self.chest.image.get_rect()
        self.chest.image = pygame.transform.scale(self.chest.image,
                                                  (self.chest.rect.width * 2, self.chest.rect.height * 2))
        self.chest.rect = self.chest.image.get_rect()
        self.chest.rect.centerx = self.dollcords[0] + (self.player.sprite.rect.width // 2)
        self.chest.rect.centery = self.dollcords[1] + (self.player.sprite.rect.height // 2) - self.bodyy
        self.chest.health = self.player.chest.health

        self.left_arm.image = self.left_armsprite1
        self.left_arm.image.set_colorkey((255, 255, 255))
        self.left_arm.rect = self.left_arm.image.get_rect()
        self.left_arm.image = pygame.transform.scale(self.left_arm.image,
                                                     (self.left_arm.rect.width * 2, self.left_arm.rect.height * 2))
        self.left_arm.rect = self.left_arm.image.get_rect()
        self.left_arm.rect.centerx = self.dollcords[0] + (self.player.sprite.rect.width // 2 + self.armx)
        self.left_arm.rect.centery = self.dollcords[1] + (self.player.sprite.rect.height // 2 + self.army)
        self.left_arm.health = self.player.left_arm.health


        self.right_arm.image = self.right_armsprite1
        self.right_arm.image.set_colorkey((255, 255, 255))
        self.right_arm.rect = self.right_arm.image.get_rect()
        self.right_arm.image = pygame.transform.scale(self.right_arm.image, (
            self.right_arm.rect.width * 2, self.right_arm.rect.height * 2))
        self.right_arm.rect = self.right_arm.image.get_rect()
        self.right_arm.rect.centerx = self.dollcords[0] + (self.player.sprite.rect.width // 2 - self.armx)
        self.right_arm.rect.centery = self.dollcords[1] + (self.player.sprite.rect.height // 2 + self.army)
        self.right_arm.health = self.player.right_arm.health


        self.head.image = self.headsprite1
        self.head.image.set_colorkey((255, 255, 255))
        self.head.rect = self.head.image.get_rect()
        self.head.image = pygame.transform.scale(self.head.image,
                                                 (self.head.rect.width * 2, self.head.rect.height * 2))
        self.head.rect = self.head.image.get_rect()
        self.head.rect.centerx = self.dollcords[0] + (self.player.sprite.rect.width // 2)
        self.head.rect.centery = self.dollcords[1] + (self.player.sprite.rect.height // 2 - self.heady)
        self.head.health = self.player.head.health


        self.left_leg.image = self.left_legsprite1
        self.left_leg.image.set_colorkey((255, 255, 255))
        self.left_leg.rect = self.left_leg.image.get_rect()
        self.left_leg.image = pygame.transform.scale(self.left_leg.image,
                                                     (self.left_leg.rect.width * 2, self.left_leg.rect.height * 2))
        self.left_leg.rect = self.left_leg.image.get_rect()
        self.left_leg.rect.centerx = self.dollcords[0] + (self.player.sprite.rect.width // 2 + self.legx)
        self.left_leg.rect.centery = self.dollcords[1] + (self.player.sprite.rect.height // 2 + self.legy)
        self.left_leg.health = self.player.left_leg.health


        self.right_leg.image = self.right_legsprite1
        self.right_leg.image.set_colorkey((255, 255, 255))
        self.right_leg.rect = self.right_leg.image.get_rect()
        self.right_leg.image = pygame.transform.scale(self.right_leg.image, (
            self.right_leg.rect.width * 2, self.right_leg.rect.height * 2))
        self.right_leg.rect = self.right_leg.image.get_rect()
        self.right_leg.rect.centerx = self.dollcords[0] + (self.player.sprite.rect.width // 2 - self.legx)
        self.right_leg.rect.centery = self.dollcords[1] + (self.player.sprite.rect.height // 2 + self.legy)
        self.right_leg.health = self.player.right_leg.health
        self.doll_group.empty()
        self.doll_group.add(self.chest, self.right_arm, self.left_arm, self.head, self.left_leg,
                            self.right_leg)
        for i in self.doll_group:
            img = i.image
            # im = Image.frombytes("RGBA", (i.rect.width, i.rect.height), img)
            for x in range(img.get_width()):
                for y in range(img.get_height()):
                    color = img.get_at((x, y))  # Preserve the alpha value.
                    try:
                        img.set_at((x, y), ((100 - i.health) * 2, color[1], color[2]))
                    except:
                        pass

            i.image = img
        self.doll_group.update()
        self.doll_group.draw(self.screen)
    def itemsinterface(self):
        pass
    def partpurpose(self):
        pass
    def partdoll(self):
        self.prtsgroup = pygame.sprite.Group()
        self.chest = pygame.sprite.Sprite()
        self.chestsprite1 = pygame.image.load("Assets/Sprites/Character_parts/Body_parts/chest.png").convert()
        self.left_arm = pygame.sprite.Sprite()
        self.left_armsprite1 = pygame.image.load("Assets/Sprites/Character_parts/Body_parts/left_arm.png").convert()
        self.right_arm = pygame.sprite.Sprite()
        self.right_armsprite1 = pygame.image.load("Assets/Sprites/Character_parts/Body_parts/right_arm.png").convert()
        self.head = pygame.sprite.Sprite()
        self.headsprite1 = pygame.image.load("Assets/Sprites/Character_parts/Body_parts/head.png").convert()
        self.left_leg = pygame.sprite.Sprite()
        self.left_legsprite1 = pygame.image.load("Assets/Sprites/Character_parts/Body_parts/left_leg.png").convert()
        self.right_leg = pygame.sprite.Sprite()
        self.right_legsprite1 = pygame.image.load("Assets/Sprites/Character_parts/Body_parts/right_leg.png").convert()
        self.chest.image = self.chestsprite1
        self.chest.image.set_colorkey((255, 255, 255))
        self.chest.rect = self.chest.image.get_rect()
        self.chest.image = pygame.transform.scale(self.chest.image,
                                                  (self.chest.rect.width * 2, self.chest.rect.height * 2))
        self.chest.rect = self.chest.image.get_rect()
        self.chest.rect.centerx = self.dollcords[0] + (self.player.sprite.rect.width // 2)
        self.chest.rect.centery = self.dollcords[1] + (self.player.sprite.rect.height // 2) - self.bodyy
        self.chest.health = self.player.chest.health

        self.left_arm.image = self.left_armsprite1
        self.left_arm.image.set_colorkey((255, 255, 255))
        self.left_arm.rect = self.left_arm.image.get_rect()
        self.left_arm.image = pygame.transform.scale(self.left_arm.image,
                                                     (self.left_arm.rect.width * 2, self.left_arm.rect.height * 2))
        self.left_arm.rect = self.left_arm.image.get_rect()
        self.left_arm.rect.centerx = self.dollcords[0] + (self.player.sprite.rect.width // 2 + self.armx)
        self.left_arm.rect.centery = self.dollcords[1] + (self.player.sprite.rect.height // 2 + self.army)
        self.left_arm.health = self.player.left_arm.health

        self.right_arm.image = self.right_armsprite1
        self.right_arm.image.set_colorkey((255, 255, 255))
        self.right_arm.rect = self.right_arm.image.get_rect()
        self.right_arm.image = pygame.transform.scale(self.right_arm.image, (
            self.right_arm.rect.width * 2, self.right_arm.rect.height * 2))
        self.right_arm.rect = self.right_arm.image.get_rect()
        self.right_arm.rect.centerx = self.dollcords[0] + (self.player.sprite.rect.width // 2 - self.armx)
        self.right_arm.rect.centery = self.dollcords[1] + (self.player.sprite.rect.height // 2 + self.army)
        self.right_arm.health = self.player.right_arm.health

        self.head.image = self.headsprite1
        self.head.image.set_colorkey((255, 255, 255))
        self.head.rect = self.head.image.get_rect()
        self.head.image = pygame.transform.scale(self.head.image,
                                                 (self.head.rect.width * 2, self.head.rect.height * 2))
        self.head.rect = self.head.image.get_rect()
        self.head.rect.centerx = self.dollcords[0] + (self.player.sprite.rect.width // 2)
        self.head.rect.centery = self.dollcords[1] + (self.player.sprite.rect.height // 2 - self.heady)
        self.head.health = self.player.head.health

        self.left_leg.image = self.left_legsprite1
        self.left_leg.image.set_colorkey((255, 255, 255))
        self.left_leg.rect = self.left_leg.image.get_rect()
        self.left_leg.image = pygame.transform.scale(self.left_leg.image,
                                                     (self.left_leg.rect.width * 2, self.left_leg.rect.height * 2))
        self.left_leg.rect = self.left_leg.image.get_rect()
        self.left_leg.rect.centerx = self.dollcords[0] + (self.player.sprite.rect.width // 2 + self.legx)
        self.left_leg.rect.centery = self.dollcords[1] + (self.player.sprite.rect.height // 2 + self.legy)
        self.left_leg.health = self.player.left_leg.health

        self.right_leg.image = self.right_legsprite1
        self.right_leg.image.set_colorkey((255, 255, 255))
        self.right_leg.rect = self.right_leg.image.get_rect()
        self.right_leg.image = pygame.transform.scale(self.right_leg.image, (
            self.right_leg.rect.width * 2, self.right_leg.rect.height * 2))
        self.right_leg.rect = self.right_leg.image.get_rect()
        self.right_leg.rect.centerx = self.dollcords[0] + (self.player.sprite.rect.width // 2 - self.legx)
        self.right_leg.rect.centery = self.dollcords[1] + (self.player.sprite.rect.height // 2 + self.legy)
        self.right_leg.health = self.player.right_leg.health


