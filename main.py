import pygame
from generate_menu import generate_menu
from start_game import start_game
from game_settings import game_settings

def main():
    # pygame template
    pygame.init()
    
    WIDTH = 760
    HEIGHT = 800
    SIZE = (WIDTH, HEIGHT)
    
    screen = pygame.display.set_mode(SIZE)
    clock = pygame.time.Clock()
    
    menu = True
    gameSettings = False
    startGame = False

    running = True
    while running:
        # EVENT HANDLING
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                # opens settings
                if menu and x >= 650 and y >= 650 \
                    and x <= 650 + 50 and y <= 650 + 50:
                    menu = False
                    startGame = False
                    gameSettings = True
                # returns to menu
                elif gameSettings and x >= 50 and y >= 50 \
                    and x <= 50 + 125 and y <= 50 + 125:
                    gameSettings = False
                    startGame = False
                    menu = True
                # starts game
                elif menu and x >= 190 and y >= 650 and \
                    x <= 190 * 3 and y <= 640 + 75: 
                    menu = False
                    gameSettings = False
                    startGame = True
            
        # GAME STATE UPDATES
    
        # if this is shown, something went wrong
        screen.fill((0, 0, 0))

        if menu:
            generate_menu(screen)
            # create a rectangle
            # on click, set menu to false
            # then the game will start
        elif gameSettings:
            game_settings(screen)
        elif startGame:
            start_game(screen)
        
        
        # Must be the last two lines of the game loop
        pygame.display.flip()
        clock.tick(30)
        
    pygame.quit()
    
    return 0

if __name__ == "__main__":
    main()