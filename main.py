import pygame 
import sys
from sfondo import sfondo


pygame.init()
window_size = (1200, 800)
screen = pygame.display.set_mode(window_size,0,32)
Display = pygame.Surface((900, 600))

pygame.display.set_caption("survival")

Sfondo = sfondo(Display)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 
    pygame.display.update()
    Sfondo.draw()
    
