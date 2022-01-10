import pygame
class PlayerInterface:
    def __init__(self, playercls, w, h, sc):
        self.screen = sc
        self.width = w
        self.height = h
        self.player = playercls
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
        self.spells = []
    def update(self):
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
            self.spells.append(pygame.image.load("Assets/Sprites/Attacks/"+i+"/Icon/"+i+".png"))
            self.spell = pygame.sprite.Sprite()
            self.spell.image = pygame.image.load("Assets/Sprites/Attacks/"+i+"/Icon/"+i+".png")
            self.spell.rect = self.spell.image.get_rect()