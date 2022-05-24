import pygame
pygame.init()

FPS = 60
n_rows = 15
n_columns = 30
block_size = 20
screen_height = n_rows * block_size
screen_width = n_columns * block_size
stickman_height = 30
stickman_width = 20
stamina_max = 200
health_max = 100
block_img_path = "/home/kiseki/PycharmProjects/Group-12-Software-Engineering/resources/block.png"
map_path = "/home/kiseki/PycharmProjects/Group-12-Software-Engineering/resources/map.txt"
database_path = "/home/kiseki/PycharmProjects/Group-12-Software-Engineering/resources/database.txt"
play_back_path = "/home/kiseki/PycharmProjects/Group-12-Software-Engineering/resources/play_back.png"
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (50, 205, 50)
BLACK = (0, 0, 0)