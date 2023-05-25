import pygame 
import sys
from math import ceil

# schermata
pygame.init()
screen_width = 1000
screen_height = 1000

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("survival")

#sfondo
foto = pygame.image.load("sfondo1.webp")
foto = pygame.transform.scale(foto, (1000, 800))
screen.blit(foto, (0,0))

#griglia
size_cella = 100 

class Mondo():
    def __init__(self, mappa):
        
        self.griglia_list = []
        
        #immagini
        cubo_foto=pygame.image.load("cubo.webp")
        
        criga = 0
        for riga in mappa:
            ccolonna = 0
            for cella in riga:
                if cella == 1:
                    img =  pygame.transform.scale(cubo_foto, (size_cella, size_cella))
                    img_rect = img.get_rect()
                    img_rect.x = ccolonna * size_cella 
                    img_rect.y = criga * size_cella 
                    cella = (img, img_rect)
                    self.griglia_list.append(cella)
                ccolonna += 1
            criga += 1
            
    def draw(self):
        for cella in self.griglia_list:
            screen.blit(cella[0], cella[1])

with open("map.txt") as f:
    mappa = [list(map(int, riga.strip().split())) for riga in f] 

mondo = Mondo(mappa)
while True:
    
    print(mondo.griglia_list)
    mondo.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 
            
    pygame.display.update()
    
    
