import pygame, sys
from sudoku_generator import *

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

    waiting_for_click = True
    while waiting_for_click:
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

def game_ip_screen(level):
    #sudoku board
    window.fill(WHITE)
    window.blit(background_image, (0, 0))
    grid_bg = pygame.Rect(50, 0, 500, 500)
    pygame.draw.rect(window, WHITE, grid_bg)
    for i in range(10):
        pygame.draw.line(window, BLACK, (i * (500/9) + 50, 0), (i * (500/9) + 50, 500))
        pygame.draw.line(window, BLACK, (50, i * (500/9)), (550, i * (500/9)))

    #reset button
    reset_button = pygame.Rect(25, 525, 150, 50)
    pygame.draw.rect(window, DARKGREEN, reset_button)
    reset_text = small_font.render("Reset", True, WHITE)
    window.blit(reset_text, (55 + reset_text.get_width() // 2, 525 + reset_text.get_height() // 2))

    #restart button
    restart_button = pygame.Rect((WIDTH - 150) // 2, 525, 150, 50)
    pygame.draw.rect(window, DARKGREEN, restart_button)
    restart_text = small_font.render("Restart", True, WHITE)
    window.blit(restart_text, ((WIDTH - restart_text.get_width()) // 2, 525 + restart_text.get_height() // 2))

    #exit button
    exit_button = pygame.Rect(WIDTH - 175, 525, 150, 50)
    pygame.draw.rect(window, DARKGREEN, exit_button)
    exit_text = small_font.render("Exit", True, WHITE)
    window.blit(exit_text, (WIDTH - 140 + (exit_text.get_width()), 525 + exit_text.get_height() // 2))

    #stuff based off of what level they chose
    if level == 1:
        print(30)
    elif level == 2:
        print(40)
    elif level == 3:
        print(50)
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
                elif restart_button.collidepoint(mouse_x, mouse_y):
                    # need to add proper reset code
                    print("fix this")
                elif reset_button.collidepoint(mouse_x, mouse_y):
                    # need to add proper reset code
                    print("fix this")

#main game load test
if __name__ == '__main__':
    pygame.init()
    WIDTH, HEIGHT = 600, 600
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Holiday Sudoku")

    # Load the custom background image
    background_image = pygame.image.load("christmas.png")
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

    level = game_start_screen()
    while True:
        if level == 30:
            game_ip_screen(30)
        elif level == 40:
            game_ip_screen(40)
        elif level == 50:
            game_ip_screen(50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()