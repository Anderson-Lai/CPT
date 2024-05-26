import pygame
from menu.generate_menu import generate_menu
from game.start_game import start_game
from gameSettings.game_settings import game_settings
from eventHandling.handle_events import handle_events
from game.lives import num_lives
from game.lives import draw_removed_hearts
from game.score import get_score
from game.score import draw_score

def main() -> int:
    # pygame template
    pygame.init()

    WIDTH = 800
    HEIGHT = 800
    SIZE = (WIDTH, HEIGHT)

    screen = pygame.display.set_mode(SIZE)
    clock = pygame.time.Clock()
    pygame.key.set_repeat(50, 25)
    
    # values changed by events
    mutable_events = {
        "running": True,
        "gameState": "menu",
        "location": 375,
        "gameDifficulty": 0,
        "sensitivity": 10,
    }

    # placeholder, testing variables
    # score variables
    enemy_kills = 4
    current_score = get_score(enemy_kills)
    high_score = 170

    # lives variables
    game_difficulty = "easy"
    lives = num_lives(game_difficulty)
    hit = True

    running: bool = True
    while running:
        # EVENT HANDLING
        changed_events = handle_events(mutable_events)
        gameState, location, gameDifficulty, sensitivity, running = \
        changed_events["gameState"], changed_events["location"], changed_events["gameDifficulty"],\
        changed_events["sensitivity"], changed_events["running"]

        # GAME STATE UPDATES
    
        # if this is shown, something went wrong
        screen.fill((0, 0, 0))

        if gameState == "menu":
            generate_menu(screen)
            # create a rectangle
            # on click, chang the 'gameState' variable
        elif gameState == "settings":
            game_settings(screen, gameDifficulty, sensitivity)
        elif gameState == "game":
            start_game(screen, location)
            draw_removed_hearts(screen, lives, hit)
            draw_score(screen, high_score, current_score)

        
        # Must be the last two lines of the game loop
        pygame.display.flip()
        clock.tick(30)
        
    pygame.quit()
    
    return 0

if __name__ == "__main__":
    result: int = main()
    if result != 0:
        print(f"Main exited with error code {result}.")
