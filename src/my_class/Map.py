from src.config import *


#Block
class Block:
    #Khoi tao block
    def __init__(self, posx, posy):
        self.posx = posx
        self.posy = posy
        self.img = pygame.image.load(block_img_path)
        self.rect = pygame.Rect(self.posx, self.posy, block_size, block_size)

    #Ve block len pygame display
    def draw(self, surface):
        surface.blit(self.img, (self.posx, self.posy))


#Map
class Map:
    #khoi tao map
    def __init__(self, path):
        self.blocks = list()
        self.load_map(path)

    #Load map tu file map.txt
    def load_map(self, path):
        with open(path) as file:
            for i in range(n_rows):
                line = file.readline()
                for j in range(len(line)):
                    if line[j] == 'b':
                        self.blocks.append(Block(j*block_size, i*block_size, ))

    #Ve map len pygame display
    def draw(self, surface):
        for b in self.blocks:
            b.draw(surface)

    #Cap nhat trang thai hien tai cua map
    def update(self):
        pass