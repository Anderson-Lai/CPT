import pygame

def start_game(screen, location):
    screen.fill((0, 255, 255))
    pygame.draw.rect(screen, (0, 255, 0), (location, 770, 50, 50))

    
