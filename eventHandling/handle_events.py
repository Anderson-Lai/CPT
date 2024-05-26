import pygame

def handle_events(events: dict) -> dict:

    gameState: str = events["gameState"]
    location: int = events["location"]
    gameDifficulty: str = events["gameDifficulty"]
    sensitivity: int = events["sensitivity"]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            events["running"] = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()

            # opens settings
            if gameState == "menu" and 650 <= x <= 650 + 100 \
            and 575 <= y <= 575 + 100:
                events["gameState"] = "settings"
            # returns to menu
            elif gameState == "settings" and 50 <= x <= 50 + 125 \
            and 50 <= y <= 50 + 125:
                events["gameState"] = "menu"
            # starts game
            elif gameState == "menu" and 175 <= x <= 175 + 450 \
            and 550 <= y <= 550 + 150:
                events["gameState"] = "game"

            # changing settings
            # changing difficulty
            elif gameState == "settings" and 300 <= x <= 300 + 200 \
            and 200 <= y <= 200 + 100:
                events["gameDifficulty"] += 1
                if gameDifficulty >= 3:
                    events["gameDifficulty"] = 0
            # incrementing sensitivity
            elif gameState == "settings" and 475 <= x <= 525 \
            and 350 <= y <= 350 + 50:
                events["sensitivity"] += 1
            # decrementing sensitivity
            elif gameState == "settings" and 275 <= x <= 325 \
            and 350 <= y <= 350 + 50:
                events["sensitivity"] -= 1
                if sensitivity <= -1:
                    events["sensitivity"] = 0
            
        #spaceship movement
        if event.type == pygame.KEYDOWN:
            # move right
            if event.key == pygame.K_RIGHT and location < 535:
                events["location"] += events["sensitivity"]
                if location - sensitivity < 25:
                    events["location"] = 25
            # move left
            elif event.key == pygame.K_LEFT and location > 25:
                events["location"] -= events["sensitivity"]
                if location + sensitivity > 600:
                    events["location"] = 590

    return events