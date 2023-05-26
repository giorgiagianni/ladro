import pygame
from math import ceil
class Piattaforma:
    def __init__(self,display,nomefile='./mappe/mappa.txt')->None:
        self.display=display
        self.bc_img = pygame.image.load('./immagini/bc_img.png')
        self.cubo_img = pygame.image.load('./immagini/cubo_img.png')
        with open(nomefile)as f:
            self.mappa=[list(map(int, riga.strip().split() ))for riga in f]
        self.numr=len(self.mappa)
        self.numc=len(self.mappa[0])
        self.w_tile=ceil(display.get_width()/self.numc)
        self.h_tile=ceil(display.get_height()/self.numr)
        self.bc_img=pygame.transform.scale(self.bc_img,(900,700))
        self.cubo_img=pygame.transform.scale(self.cubo_img,(self.w_tile,self.h_tile))
        self.listaBlocchi=[]
        self.griglia=[]
        for y, r in enumerate(self.mappa):
            for x,cella in enumerate(r):
                if cella!=0:
                    self.griglia.append(pygame.Rect(x*self.w_tile,y*self.h_tile,self.w_tile,self.h_tile))
    def crea(self):
        self.display.blit(self.bc_img,(0,0))
        for y,r in enumerate(self.mappa):
            for x, cella in enumerate(r):
                if cella==1:
                    self.display.blit(self.cubo_img,(x*self.w_tile,y*self.h_tile))
                    
                # if cella==2:
                #     self.display.blit(self.minicubo_img,(x*self.w_tile,y*self.h_tile))

