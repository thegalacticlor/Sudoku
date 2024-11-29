import pygame, sys

def game_won_screen():
    window.fill(WHITE)
    window.blit(background_image, (0, 0))
    text = font.render("Game Won!", True, GREEN)
    text_width = text.get_width()
    text_height = text.get_height()
    window.blit(text, ((WIDTH - text_width) // 2, (HEIGHT - text_height) // 3))

    exit_button = pygame.Rect((WIDTH - 200) // 2, HEIGHT // 2, 200, 50)
    pygame.draw.rect(window, GREEN, exit_button)
    exit_text = small_font.render("Exit", True, WHITE)
    exit_text_width = exit_text.get_width()
    exit_text_height = exit_text.get_height()
    window.blit(exit_text, ((WIDTH - exit_text_width) // 2, (HEIGHT // 2) + (50 - exit_text_height) // 2))

    pygame.display.update()

    waiting_for_click = True
    while waiting_for_click:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if exit_button.collidepoint(mouse_x, mouse_y):
                    pygame.quit()
                    quit()

def game_lost_screen():
    window.fill(WHITE)
    window.blit(background_image, (0, 0))
    text = font.render("Game Over :(", True, RED)
    text_width = text.get_width()
    text_height = text.get_height()
    window.blit(text, ((WIDTH - text_width) // 2, (HEIGHT - text_height) // 3))

    restart_button = pygame.Rect((WIDTH - 200) // 2, HEIGHT // 2, 200, 50)
    pygame.draw.rect(window, RED, restart_button)
    restart_text = small_font.render("Restart", True, WHITE)
    restart_text_width = restart_text.get_width()
    restart_text_height = restart_text.get_height()
    window.blit(restart_text, ((WIDTH - restart_text_width) // 2, (HEIGHT // 2) + (50 - restart_text_height) // 2))

    pygame.display.update()

    waiting_for_click = True
    while waiting_for_click:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if restart_button.collidepoint(mouse_x, mouse_y):
                    return True
    return False

def game_start_screen():
    window.fill(WHITE)
    window.blit(background_image, (0, 0))

    #welcome text
    textOne = fancy_font.render("Welcome to Sudoku!", True, RED)
    window.blit(textOne, ((WIDTH - textOne.get_width()) // 2, (HEIGHT - textOne.get_height()) // 3 - 100))

    #extra bottom text
    textTwo = small_fancy_font.render("Choose a difficulty:", True, GREEN)
    window.blit(textTwo, ((WIDTH - textTwo.get_width()) // 2, (HEIGHT - textTwo.get_height()) // 3))

    #easy button
    easy_button = pygame.Rect((WIDTH - 200) // 2, HEIGHT // 2, 200, 50)
    pygame.draw.rect(window, RED, easy_button)
    easy_text = small_font.render("Easy", True, WHITE)
    window.blit(easy_text, ((WIDTH - easy_text.get_width()) // 2, (HEIGHT // 2) + (50 - easy_text.get_height()) // 2))

    #medium button
    medium_button = pygame.Rect((WIDTH - 200) // 2, HEIGHT // 2 + 75, 200, 50)
    pygame.draw.rect(window, RED, medium_button)
    medium_text = small_font.render("Medium", True, WHITE)
    window.blit(medium_text, ((WIDTH - medium_text.get_width()) // 2, (HEIGHT // 2) + (200 - medium_text.get_height()) // 2))

    #hard button
    hard_button = pygame.Rect((WIDTH - 200) // 2, HEIGHT // 2 + 150, 200, 50)
    pygame.draw.rect(window, RED, hard_button)
    hard_text = small_font.render("Hard", True, WHITE)
    window.blit(hard_text,((WIDTH - hard_text.get_width()) // 2, (HEIGHT // 2) + (350 - hard_text.get_height()) // 2))

    pygame.display.update()

    noInput = True
    while noInput:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if easy_button.collidepoint(mouse_x, mouse_y):
                    return 30
                elif medium_button.collidepoint(mouse_x, mouse_y):
                    return 40
                elif hard_button.collidepoint(mouse_x, mouse_y):
                    return 50

#main game load test
def main():
    pygame.init()

    WIDTH, HEIGHT = 600, 600
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Holiday Sudoku")

    # Load the custom background image
    background_image = pygame.image.load("christmasBackground.jpg")
    background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))  # Resize to fit the window

    # Define colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (113, 163, 108)
    DARKGREEN = (42, 74, 39)
    RED = (235, 55, 52)

    # Fonts
    font = pygame.font.SysFont("arial", 40)
    small_font = pygame.font.SysFont("arial", 20)
    fancy_font = pygame.font.SysFont("gabriola", 60)
    small_fancy_font = pygame.font.SysFont("gabriola", 45)

    while True:
        level = game_start_screen()
        if level == 30:
            # do something cause 30
            print("30")
        elif level == 40:
            # do something cause 40
            print("40")
        elif level == 50:
            # do something cause 50
            print("50")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

if __name__ == '__main__':
    main()