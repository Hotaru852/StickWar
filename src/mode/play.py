from src.my_class.Map import Map
from src.my_class.Player import StickMan
from src.config import *
from src.my_class.Item import Bow, Spear
import pygame


#Pygame display
class Play_Scene:
    #Khoi tao play_scene
    def __init__(self):
        self.turn = 0
        self.score = None
        self.players = []
        self.weapon = None
        self.map = Map(map_path)
        self.bow_level = None
        self.spear_level = None
        self.potion_level = None
        self.state = True
        self.winner = None

    #Setup play_scene
    def setup(self, n):
        for i in range(n):
            self.players.append(StickMan(RED, self.potion_level, self.map))
            self.players.append(StickMan(BLUE, self.potion_level, self.map))
        self.score = n * 200

    #Ve len pygame display
    def draw(self, screen: pygame.Surface):
        screen.blit(pygame.image.load(play_back_path), (0, 0))
        self.map.draw(screen)
        for i in self.players:
            i.draw(screen)
        if self.weapon is not None:
            self.weapon.draw(screen)

    #Trang thai hoat dong cua play_scene
    def active(self):
        return self.state

    #Cap nhat play_scene
    def update(self, events):
        for player in self.players:
            player.update(events)
            if not player.is_alive:
                self.players.remove(player)
        red_players = 0
        for player in self.players:
            if player.color == RED:
                red_players += 1
        # if all player of red or blue died, game end
        if red_players == 0 or red_players == len(self.players):
            self.state = False
            if red_players == 0:
                self.winner = "BLUE"
            else:
                self.winner = "RED"
            return
        current_player = self.players[self.turn]
        if not current_player.turn:
            current_player.turn = True
        if current_player.turn:
            if current_player.aiming:
                if current_player.shooting:
                    if not self.weapon.active:
                        self.weapon.active = True
                    if self.weapon.stop:
                        current_player.aiming = False
                        current_player.shooting = False
                        self.turn = (self.turn + 1) % len(self.players)
                        self.score -= 1
                        current_player.turn = False
                        current_player.sta = stamina_max
                        self.weapon = None
                    else:
                        self.weapon.update()
                else:
                    if self.weapon is None:
                        if current_player.weapon == 1:
                            self.weapon = (Bow(int(self.bow_level), current_player, self.map, self.players))
                        elif current_player.weapon == 2:
                            self.weapon = (Spear(int(self.spear_level), current_player, self.map, self.players))
                    self.weapon.update()
            elif not current_player.heal_available:
                current_player.turn = False
                current_player.sta = stamina_max
                current_player.heal_available = True
                self.turn = (self.turn + 1) % len(self.players)
                self.score -= 1