import pygame
from math import ceil

class sfondo():
    def __init__(self, display, nomefile= "map.txt"):
        self.display= display
        self.grass = pygame.image.load("sfondo1.webp")
        self.cubo = pygame.image.load("cubo.webp")
        with open(nomefile) as f:
            self.mappa = [list(map(int, riga.strip().split())) for riga in f]
        self.righe = len(self.mappa)
        self.colonne = len(self.mappa[0])
        self.l_cella=ceil(display.get_width()/ self.colonne)
        self.h_cella=ceil(display.get_hight()/ self.righe)
        self.cubo=pygame.transform.scale(self.cubo, (self.l_cella, self.h_cella))
        self.griglia=[]
        for y, riga in enumerate(self.mappa):
            for x, cella in enumerate(riga):
                if cella !=0:
                    self.griglia.append(pygame.Rect(x*self.l_cella, y*self.h_cella))
                    
    def draw(self):
        self.display.update(self.grass)
        for y, riga in enumerate(self.mappa):
            for x, cella in enumerate(riga):
                if cella == 1:
                    self.display.blit(self.cubo, (x*self.l_cella, y*self.h_cella))
