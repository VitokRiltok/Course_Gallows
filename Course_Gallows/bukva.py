import pygame
import sys

def run():

    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Виселица")
    bg_color = (128, 128, 128)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(bg_color) 
        pygame.display.flip()        
    
run ()
