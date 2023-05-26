import pygame
import os
import random

dir_path = os.path.dirname(os.path.realpath(__file__))

os.chdir(dir_path)

pygame.init()

window = pygame.display.set_mode((900,500))

pygame.mouse.set_visible(False)

running = True

clock = pygame.time.Clock()
fps = 60

class assets:
    grass = pygame.transform.scale(pygame.image.load(f"{dir_path}/grass.gif").convert_alpha(),(100,100))
    dirt = pygame.transform.scale(pygame.image.load(f"{dir_path}/dirt.gif").convert_alpha(),(100,100))
    stone = pygame.transform.scale(pygame.image.load(f"{dir_path}/stone.gif").convert_alpha(),(100,100))
    forest = pygame.transform.scale(pygame.image.load(f"{dir_path}/forest.gif").convert_alpha(),(100,100))
    cursor = pygame.transform.scale(pygame.image.load(f"{dir_path}/world_cursor.gif").convert_alpha(),(30,30))

selection1 = [assets.grass,assets.dirt,assets.stone,assets.forest]

class map:
    def __init__(self):
        self.tiles = []
        self.seed = []
        self.seedText = "hi"
    def gen(self):
        self.tiles = []
        self.seed = []
        for i in range(5):
            row = []
            seedRow = []
            for o in range(9):
                randal = random.randint(0,len(selection1) - 1)
                value = selection1[randal]
                row.append(value)
                seedRow.append(selection1.index(value))
            self.tiles.append(row)
            self.seed.append(seedRow)
        self.seedText = ''.join([str(value) for row in self.seed for value in row])
    def load(self,seed):
        print(self.seedText)
        self.tiles = []
        for i in range(5):
            row = []
            seedRow = []
            for o in range(9):
                value = selection1[int(seed[(i * 9) + o])]  
                print(int(seed[(i * 9) + o]),end="")
                row.append(value)
                seedRow.append(selection1.index(value))
            self.tiles.append(row)
            self.seed.append(seedRow)
        self.seedText = seed
        print("\n")
        print(self.seedText)
            
    def render(self):
        map_x = 0
        map_y = 0
        for i in range(5):
            for o in range(9):
                window.blit(self.tiles[i][o], (map_x,map_y))
                map_x += 100
            map_x = 0
            map_y += 100
        
        '''
        for i in range(10):
            for o in range(10):
                self.tiles[].append(selection1[random.randint(0,len(selection1) - 1)], (map_x,map_y)))
                map_x += 1
            map_x = 0
            map_y += 1'''
        
map1 = map()
map1.gen()

searchCount = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                map1.gen()
                print(map1.seedText)
            if pygame.mouse.get_pressed()[2]:

                ##### FOR SEED LOADING PASTE SEED HERE #####

                map1.load("000000000000011100000112200000111100000010100")
    pygame.display.set_caption(f"{searchCount}")
    #if "0" in map1.seedText:
     #   searchCount += 1
      #  map1.gen()

    pygame.display.update()
    clock.tick(fps)
    map1.render()
    #window.blit(assets.grass, (0,0))
    window.blit(assets.cursor, pygame.mouse.get_pos())

pygame.quit