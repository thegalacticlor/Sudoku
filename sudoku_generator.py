import math, random, time
import pygame

"""
This was adapted from a GeeksforGeeks article "Program for Sudoku Generator" by Aarti_Rathi and Ankur Trisal
https://www.geeksforgeeks.org/program-sudoku-generator/
"""

pygame.init()

WIDTH, HEIGHT = 600, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku Game")

# Load the custom background image
background_image = pygame.image.load("christmas.png")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))  # Resize to fit the window

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Fonts
font = pygame.font.SysFont("arial", 40)
small_font = pygame.font.SysFont("arial", 20)


class SudokuGenerator:
    '''
    create a sudoku board - initialize class variables and set up the 2D board
    This should initialize:
    self.row_length        - the length of each row
    self.removed_cells    - the total number of cells to be removed
    self.board            - a 2D list of ints to represent the board
    self.box_length        - the square root of row_length

    Parameters:
    row_length is the number of rows/columns of the board (always 9 for this project)
    removed_cells is an integer value - the number of cells to be removed

    Return:
    None
    '''

    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = [[], [], [],
                      [], [], [],
                      [], [], []]
        self.box_length = row_length ** .5

    '''
    	Returns a 2D python list of numbers which represents the board

    	Parameters: None
    	Return: list[list]
    '''

    def get_board(self):
        return self.board

    '''
    	Displays the board to the console
        This is not strictly required, but it may be useful for debugging purposes

    	Parameters: None
    	Return: None
    
    '''
    def print_board(self):
        pass

    '''
    	Determines if num is contained in the specified row (horizontal) of the board
        If num is already in the specified row, return False. Otherwise, return True

    	Parameters:
    	row is the index of the row we are checking
    	num is the value we are looking for in the row

    	Return: boolean
    '''

    def valid_in_row(self, row, num):
        pass

    '''
    	Determines if num is contained in the specified column (vertical) of the board
        If num is already in the specified col, return False. Otherwise, return True

    	Parameters:
    	col is the index of the column we are checking
    	num is the value we are looking for in the column

    	Return: boolean
    '''

    def valid_in_col(self, col, num):
        pass

    '''
    	Determines if num is contained in the 3x3 box specified on the board
        If num is in the specified box starting at (row_start, col_start), return False.
        Otherwise, return True

    	Parameters:
    	row_start and col_start are the starting indices of the box to check
    	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)
    	num is the value we are looking for in the box

    	Return: boolean
    '''

    def valid_in_box(self, row_start, col_start, num):
        pass

    '''
        Determines if it is valid to enter num at (row, col) in the board
        This is done by checking that num is unused in the appropriate, row, column, and box

    	Parameters:
    	row and col are the row index and col index of the cell to check in the board
    	num is the value to test if it is safe to enter in this cell

    	Return: boolean
    '''

    def is_valid(self, row, col, num):
        pass

    '''
        Fills the specified 3x3 box with values
        For each position, generates a random digit which has not yet been used in the box

        Parameters:
        row_start and col_start are the starting indices of the box to check
        i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)

        Return: None
    '''

    def fill_box(self, row_start, col_start):
        pass

    '''
        Fills the three boxes along the main diagonal of the board
        These are the boxes which start at (0,0), (3,3), and (6,6)

    	Parameters: None
    	Return: None
    '''

    def fill_diagonal(self):
        for count in range(len(self.board)):
            if count in (0, 4, 8):
                self.board[count] = ([1, 2, 3, 4, 5, 6, 7, 8, 9])
                random.shuffle(self.board[count])

    '''
        DO NOT CHANGE
        Provided for students
        Fills the remaining cells of the board
        Should be called after the diagonal boxes have been filled

    	Parameters:
    	row, col specify the coordinates of the first empty (0) cell

    	Return:
    	boolean (whether or not we could solve the board)
    '''

    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    '''
        DO NOT CHANGE
        Provided for students
        Constructs a solution by calling fill_diagonal and fill_remaining

    	Parameters: None
    	Return: None
    '''

    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    '''
        Removes the appropriate number of cells from the board
        This is done by setting some values to 0
        Should be called after the entire solution has been constructed
        i.e. after fill_values has been called

        NOTE: Be careful not to 'remove' the same cell multiple times
        i.e. if a cell is already 0, it cannot be removed again

    	Parameters: None
    	Return: None
    '''

    def remove_cells(self):
        pass

    '''
    DO NOT CHANGE
    Provided for students
    Given a number of rows and number of cells to remove, this function:
    1. creates a SudokuGenerator
    2. fills its values and saves this as the solved state
    3. removes the appropriate number of cells
    4. returns the representative 2D Python Lists of the board and solution

    Parameters:
    size is the number of rows/columns of the board (9 for this project)
    removed is the number of cells to clear (set to 0)

    Return: list[list] (a 2D Python list to represent the board)
    '''

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


def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board
