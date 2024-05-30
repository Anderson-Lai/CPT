import pygame

"""
start game button
permanent upgrades (the shop)
settings
difficulty button 
"""

def generate_menu(screen):
    screen.fill((0, 0, 0))

    # open shop
    pygame.draw.rect(screen, (169, 169, 169), pygame.Rect(650, 450, 100, 100))

    # open settings
    pygame.draw.rect(screen, (211, 211, 211), pygame.Rect(650, 575, 100, 100))
    settings_icon = pygame.image.load("settings_icon.png")
    smaller_settings_icon = pygame.transform.scale(settings_icon, (85, 85))
    screen.blit(settings_icon_small, (659, 582.5))

    # start game button
    pygame.draw.rect(screen, (255, 255, 237), pygame.Rect(175, 550, 450, 150))
