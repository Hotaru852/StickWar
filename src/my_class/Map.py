from src.config import *


class Block:
    def __init__(self, posx, posy):
        self.posx = posx
        self.posy = posy
        self.img = pygame.image.load(block_img_path)
        self.rect = pygame.Rect(self.posx, self.posy, block_size, block_size)

    def draw(self, surface):
        surface.blit(self.img, (self.posx, self.posy))


class Map:
    def __init__(self, path):
        self.blocks = list()
        self.load_map(path)

    def load_map(self, path):
        with open(path) as file:
            for i in range(n_rows):
                line = file.readline()
                for j in range(len(line)):
                    if line[j] == 'b':
                        self.blocks.append(Block(j*block_size, i*block_size, ))

    def draw(self, surface):
        for b in self.blocks:
            b.draw(surface)

    def update(self):
        pass