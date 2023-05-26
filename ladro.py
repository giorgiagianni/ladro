import pygame
from pygame.locals import*
from piattaforma import Piattaforma
def collision_test(rect, tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list


class Ladro:
    def __init__(self,display,piattaforma,pos,size,vel_orizz = 5, forza_jump = 18)->None:
        self.display=display
        self.piattaforma=piattaforma
        self.gravità=0.3
        self.vel_orizz = vel_orizz
        self.forza_jump = forza_jump
        self.maxvel=8
        self.size=size
        self.ladro_img=pygame.image.load('./immagini/player.png')
        self.ladro_img=pygame.transform.scale(self.ladro_img,self.size)
        self.rect=pygame.Rect((pos[0],pos[1]), (size[0],size[1]))
        self.image=self.ladro_img
        self.moving_r=False
        self.moving_l=False
        self.falling=True
        self.velvet=[0,0]
        self.jumping=True
        self.collision = {'top': False, 'bottom': False, 'right': False, 'left': False}
    def move_r(self):
        self.moving_r=True
        self.moving_l=False
    def stop_move_r(self):
        self.moving_r=False
    def move_l(self):
        self.moving_r=False
        self.moving_l=True
    def stop_move_l(self):
        self.moving_l=False
    
    def move(self):
        collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}
        if self.moving_r:
            self.velvet[0] = self.vel_orizz
        elif self.moving_l:
            self.velvet[0] = -self.vel_orizz
        else: 
            self.velvet[0] = 0
        self.rect.x += self.velvet[0]

        hit_list = collision_test(self.rect, self.piattaforma.griglia)
        for tile in hit_list:
            
            if self.velvet[0] > 0:
                self.rect.right = tile.left
                collision_types['right'] = True
            
            if self.velvet[0] < 0:
                self.rect.left = tile.right
                collision_types['left'] = True

        
        self.velvet[1] += self.gravità
        if self.velvet[1] > self.maxvel:
            self.velvet[1] = self.maxvel
        self.rect.y += self.velvet[1]

        hit_list = collision_test(self.rect, self.piattaforma.griglia)
        for tile in hit_list:
            
            if self.velvet[1] > 0:
                self.rect.bottom = tile.top
                collision_types['bottom'] = True
           
            if self.velvet[1] < 0:
                self.rect.top = tile.bottom
                collision_types['top'] = True
                self.velvet[1] = 0

        if self.rect.left < 0:
            self.rect.left = 0 
        if self.rect.right > self.display.get_width():
            self.rect.right = self.display.get_width()

        if collision_types['bottom']:
            self.jumping = False


    def salto(self):
        if not self.jumping:
            self.velvet[1] -= self.forza_jump
            self.jumping = True


    def draw(self):
        self.display.blit(self.image,(self.rect.x,self.rect.y))
