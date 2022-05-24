import random
from src.my_class.Map import Map
from src.config import *


#Stickman
class StickMan:
    #Khoi tao stickman
    def __init__(self, color, potion_level,  map=Map(map_path)):
        self.image = pygame.image.load("/home/kiseki/PycharmProjects/Group-12-Software-Engineering/resources/figure-L1.gif")
        self.images_left = [
            pygame.image.load("/home/kiseki/PycharmProjects/Group-12-Software-Engineering/resources/figure-L1.gif"),
            pygame.image.load("/home/kiseki/PycharmProjects/Group-12-Software-Engineering/resources/figure-L2.gif"),
            pygame.image.load("/home/kiseki/PycharmProjects/Group-12-Software-Engineering/resources/figure-L3.gif")
        ]
        self.images_right = [
            pygame.image.load("/home/kiseki/PycharmProjects/Group-12-Software-Engineering/resources/figure-R1.gif"),
            pygame.image.load("/home/kiseki/PycharmProjects/Group-12-Software-Engineering/resources/figure-R2.gif"),
            pygame.image.load("/home/kiseki/PycharmProjects/Group-12-Software-Engineering/resources/figure-R3.gif")
        ]
        self.health = health_max
        self.color = color
        self.v_jump = 0
        self.map = map
        self.drop = True
        self.rect = pygame.Rect(random.uniform(0, screen_width), 0, stickman_width, stickman_height)
        self.shooting = False
        self.aiming = False
        self.facing = "left"
        self.turn = False
        self.is_alive = True
        self.sta = stamina_max
        self.heal_available = True
        self.end_turn = False
        self.weapon = None
        self.heal_level = potion_level

    #Di chuyen stickman sang ben trai
    def move_left(self, map: Map):
        if self.sta <= 0:
            return
        self.sta -= 1
        self.image = self.images_left[(pygame.time.get_ticks() % 600) // 200]
        self.rect = self.rect.move(-1, 0)
        self.facing = "left"
        for i in map.blocks:
            if self.rect.colliderect(i.rect):
                self.rect = self.rect.move(1, 0)
                return

    #Di chuyen stickman sang ben phai
    def move_right(self, map: Map):
        if self.sta <= 0:
            return
        self.sta -= 1
        self.image = self.images_right[(pygame.time.get_ticks() % 600) // 200]
        self.rect = self.rect.move(1, 0)
        self.facing = "right"
        for i in map.blocks:
            if self.rect.colliderect(i.rect):
                self.rect = self.rect.move(-1, 0)
                return

    #Stickman roi tu do
    def dropping(self):
        if self.drop:
            self.rect = self.rect.move(0, 1 - self.v_jump)

        num_collided = 0
        for i in self.map.blocks:
            if self.rect.colliderect(i.rect):
                self.rect = self.rect.move(0, self.v_jump - 1)
                if self.rect.top < i.rect.top:
                    num_collided += 1
                break
        self.drop = (num_collided == 0)

    #Stickman di chuyen
    def move(self, map: Map, events):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and not self.aiming:
            self.move_left(map)
        if key[pygame.K_RIGHT] and not self.aiming:
            self.move_right(map)
        if key[pygame.K_SPACE] and not self.aiming and not self.drop:
            self.v_jump = 13
        if key[pygame.K_1] and not self.aiming and not self.drop:
            self.aiming = True
            self.weapon = 1
        if key[pygame.K_2] and not self.aiming and not self.drop:
            self.aiming = True
            self.weapon = 2

        for e in events:
            if e.type == pygame.MOUSEBUTTONDOWN and self.aiming:
                self.shooting = True
            elif e.type == pygame.KEYDOWN and self.heal_available and self.health < health_max and not self.drop and not self.aiming:
                if e.key == pygame.K_3:
                    self.health += 20 * self.heal_level
                    self.heal_available = False
                    if self.health >= health_max:
                        self.health = health_max

        # jump
        if self.v_jump > 0:
            self.v_jump -= 1

    #Cap nhat trang thai hien tai cua stickman
    def update(self, events):
        self.dropping()
        self.check_alive()
        if self.turn:
            self.move(self.map, events)

    #Ve stickman len pygame display
    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)
        pygame.draw.rect(surface, (200, 200, 200), ((self.rect.left, self.rect.top - 5), (stickman_width, 5)))
        pygame.draw.rect(surface, self.color, ((self.rect.left, self.rect.top - 5), (stickman_width * self.health/health_max, 5)))
        if self.turn:
            pygame.draw.rect(surface, (200, 200, 200), ((self.rect.left, self.rect.top - 10), (stickman_width, 5)))
            pygame.draw.rect(surface, GREEN, ((self.rect.left, self.rect.top - 10), (stickman_width * self.sta/stamina_max, 5)))
            pygame.draw.circle(surface, RED, self.rect.move(stickman_width/2, -12).topleft, 2)

    #Kiem tra xem stickman con song khong
    def check_alive(self):
        if not self.rect.colliderect(pygame.Rect(0, 0, screen_width, screen_height)) or self.health <= 0:
            self.is_alive = False