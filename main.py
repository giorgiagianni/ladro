import pygame, sys
from pygame.locals import*
from piattaforma import Piattaforma
from ladro import Ladro


window_size=(900,700)
screen=pygame.display.set_mode(window_size)
display=pygame.Surface((900,700))
piattaforma=Piattaforma(display)

pygame.display.set_caption('Survival')

clock=pygame.time.Clock()
fps=60

player=Ladro(screen,piattaforma,(100,100),(100,200))
# def move():
#         movement_types= {'top': False, 'bottom': False, 'right': False, 'left': False}

while True:
    

    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    
    keys=pygame.key.get_pressed()
    if keys[K_RIGHT]:
        player.move_r()
    else:
        player.stop_move_r()
    if keys[K_LEFT]:
        player.move_l()
    else:
        player.stop_move_l()
    if keys[K_SPACE]:
        player.salto()

    piattaforma.crea()

    surf = pygame.transform.scale(display, window_size)
    screen.blit(surf, (0,0))
    player.move()

    player.draw()

    pygame.display.update()
    clock.tick(fps)

    


       