import pygame 
import sys

pygame.init()
display = pygame.display.set_mode((800,1000))
pygame.display.set_caption("ladro")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 
    pygame.display.update()