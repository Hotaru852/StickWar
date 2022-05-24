import math
import pygame
from src.config import stickman_width, screen_width, screen_height
import functools

bow_sprites = ["Bow level 1.png", "Bow level 2.png", "Bow level 3.png", "Bow level 4.png"]
spear_sprites = ["Spear level 1.png", "Spear level 2.png", "Spear level 3.png", "Spear level 4.png"]


#Vu khi
class Weapon:
    #Khoi tao vu khi
    def __init__(self, level, stickman, map, players):
        self.angle = 0
        self.active_angle = 0
        self.active = False
        self.stop = False
        self.level = level
        self.stickman = stickman
        self.map = map
        self.targets = players
        self.image = None
        self.time = 0
        self.power = 60
        self.rect = None
        self.offset = 0
        self.startX = stickman.rect.left
        if stickman.facing == "right":
            self.startX += stickman_width
        self.startY = stickman.rect.top

    #Kiem tra va cham
    def check_for_collision(self):
        for player in self.targets:
            if self.rect.colliderect(player.rect) and player != self.stickman:
                player.health -= 20 + 10 * self.level
                self.stop = True
                return
        if not self.rect.colliderect(pygame.Rect(0, 0, screen_width, screen_height)):
            self.stop = True
            return
        for block in self.map.blocks:
            if self.rect.colliderect(block.rect):
                self.stop = True
                return

    #Tim goc
    def findAngle(self):
        pos = pygame.mouse.get_pos()
        try:
            self.angle = math.atan((self.rect.centery - pos[1]) / (self.rect.centerx - pos[0]))
        except ZeroDivisionError:
            self.angle = math.pi / 2
        if pos[1] < self.rect.centery and pos[0] > self.rect.centerx:
            self.angle = abs(self.angle)
        elif pos[1] < self.rect.centery and pos[0] < self.rect.centerx:
            self.angle = math.pi - self.angle
        elif pos[1] > self.rect.centery and pos[0] < self.rect.centerx:
            self.angle = math.pi + abs(self.angle)
        elif pos[1] > self.rect.centery and pos[0] > self.rect.centerx:
            self.angle = (math.pi * 2) - self.angle
        self.active_angle = self.angle

    #Cap nhat trang thai hien tai cua trang bi
    def update(self):
        if not self.active:
            self.findAngle()
        else:
            self.check_for_collision()
            if not self.stop:
                self.trajectory()

    #Duong bay cua vu khi
    def trajectory(self):
        pass

    #Ve vu khi len pygame display
    def draw(self, screen):
        rotated_image = pygame.transform.rotate(self.image, math.degrees(self.active_angle) + self.offset)
        new_rect = rotated_image.get_rect(center=self.image.get_rect(topleft=self.rect.topleft).center)
        screen.blit(rotated_image, new_rect.topleft)


#Bow (class con cua Weapon)
class Bow(Weapon):
    #Khoi tao Bow
    def __init__(self, level, stickman, map, players):
        super(Bow, self).__init__(level, stickman, map, players)
        self.image = pygame.image.load("/home/kiseki/PycharmProjects/Group-12-Software-Engineering/resources/" + bow_sprites[self.level - 1])
        self.rect = self.image.get_rect(center=(self.startX, self.startY))

    #Cap nhat trang thai hien tai cua Bow
    def update(self):
        if self.active:
            self.change()
        super(Bow, self).update()

    #Duong bay cua cung ten
    def trajectory(self):
        newX = round(math.cos(self.angle) * self.power * self.time + self.startX)
        newY = round(self.startY - (math.sin(self.angle) * self.power * self.time) - ((-9.8 * (self.time ** 2)) / 2))
        self.active_angle = math.atan2(self.rect.top - newY, newX - self.rect.left)
        self.rect.left = newX
        self.rect.top = newY
        self.time += 0.05

    #Thay doi hinh anh cua bow
    @functools.lru_cache(maxsize=1)
    def change(self):
        self.image = pygame.image.load("/home/kiseki/PycharmProjects/Group-12-Software-Engineering/resources/Arrow.PNG")
        self.rect = self.image.get_rect(center=(self.startX, self.startY))


#Spear (class con cua Weapon)
class Spear(Weapon):
    #Khoi tao spear
    def __init__(self, level, stickman, map, players):
        super(Spear, self).__init__(level, stickman, map, players)
        self.image = pygame.image.load("/home/kiseki/PycharmProjects/Group-12-Software-Engineering/resources/" + spear_sprites[self.level - 1])
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect(center=(self.startX, self.startY))
        self.offset = -40

    #Duong bay cua spear
    def trajectory(self):
        if self.time != self.power:
            self.rect.left += round(math.cos(self.angle))
            self.rect.top -= round(math.sin(self.angle))
        else:
            self.stop = True
        self.time += 1