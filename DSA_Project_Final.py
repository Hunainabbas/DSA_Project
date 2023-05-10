import pygame
import time
import random

# Initialize Pygame
pygame.init()
font = pygame.font.Font(None, 50)

# Set up the display window
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set the caption of the window
pygame.display.set_caption("Knight's Tour")




# Define the knight's moves
MOVES = [
    (-2, -1), (-2, 1), (-1, -2), (-1, 2),
    (1, -2), (1, 2), (2, -1), (2, 1)
]

# importing knight's picture
knight = pygame.image.load("Knight1.jpeg").convert_alpha()

# input module
def take_input():
    # Initialize input_str variable
    input_str = ''
    
    # Define error message and its rect
    error_message = font.render("Error!!!", True, (255, 0, 0)).convert_alpha()
    error_rect = error_message.get_rect(midleft=(random.randint(0, 300), random.randint(50, 700)))
    
    # Run the loop until user presses enter
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                # Check for enter key
                if event.key == pygame.K_RETURN:
                    try:
                        # Try to convert input_str to an integer
                        n = int(input_str)
                        if n < 5:
                            # Raise ValueError if n is less than 4
                            raise ValueError("Board Size must be greater than 4")
                        # Exit the function with the integer value
                        return n
                    except ValueError:
                        # If input_str cannot be converted to an integer or is less than 4, show error message
                        error_message = font.render("Error!!!", True, (255, 0, 0)).convert_alpha()
                        error_rect = error_message.get_rect(midleft=(random.randint(0, 300), random.randint(0, 700)))
                        screen.blit(error_message, error_rect)
                        pygame.display.update()
                        # Wait for a short duration before clearing the error message
                        time.sleep(0.5)
                        # Clear the error message from the screen
                        screen.blit(pygame.Surface(error_rect.size), error_rect)
                        pygame.display.update()
                        input_str = ''
                elif event.key == pygame.K_BACKSPACE:
                    # Remove last character from input_str
                    input_str = input_str[:-1]
                else:
                    # Add the character to input_str
                    input_str += event.unicode
        
        # Draw the input box
        input_rect = pygame.Rect(200, 375, 400, 50)
        pygame.draw.rect(screen, (255, 255, 255), input_rect)
        pygame.draw.rect(screen, (0, 0, 0), input_rect, 2)
        input_text = font.render(input_str, True, (0, 0, 0))
        text_rect = input_text.get_rect(midleft=(250, 400))
        screen.blit(input_text, text_rect)
        
        # Update the display
        pygame.display.update()

# Define the chessboard parameters
# N = None
# while N is None:
N = take_input()
SQUARE_SIZE = (WIDTH - 100) // N

# quitting function
def quit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

# Define a function to draw the chessboard
def draw_board():
    border_rect = pygame.Rect(0,0, 800, 800)
    pygame.draw.rect(screen, (110, 110, 110), border_rect)
    colors = [(240, 240, 240), (0, 0, 0)]
    for i in range(N):
        for j in range(N):
            color = colors[(i + j) % 2]
            rect = pygame.Rect(j * SQUARE_SIZE + 50, i * SQUARE_SIZE + 50, SQUARE_SIZE, SQUARE_SIZE)
            pygame.draw.rect(screen, color, rect)

# Define a function to draw the knight
def draw_knight(position):
    x, y = position
    rect = pygame.Rect(x * SQUARE_SIZE + 50, y * SQUARE_SIZE + 50, SQUARE_SIZE, SQUARE_SIZE)
    pygame.draw.rect(screen, (255, 0, 0), rect)

def animate_knight(screen, start_row, start_col, end_row, end_col, N, knight):
    square_size = (screen.get_width() - 100) // N
    knight_size = square_size # adjust size to fit in square
    knight_img = pygame.transform.scale(knight, (knight_size, knight_size))

    # Calculate the initial position of the knight
    x = (start_col * square_size) + 50
    y = (start_row * square_size) + 50

    # Calculate the target position of the knight
    target_x = (end_col * square_size) + 50
    target_y = (end_row * square_size) + 50

    # Calculate the amount to move the knight each frame
    dx = (target_x - x) / 10
    dy = (target_y - y) / 10

    # Loop 10 times, updating the position of the knight each frame
    for i in range(10):
        x += dx
        y += dy

        # Clear the screen
        screen.fill((255, 255, 255))

        # Draw the board
        draw_board()

        # Draw the knight at the updated position
        screen.blit(knight_img, (x, y))

        # Update the display
        pygame.display.flip()

        # Wait for a short amount of time before continuing the loop
        pygame.time.wait(50)

# Define the Knight's tour algorithm - Main Algorithm
def knight_tour():
    visited = [[False for _ in range(N)] for _ in range(N)]
    x, y = 2, 2
    visited[x][y] = True
    draw_knight((x, y))
    pygame.display.update()
    time.sleep(0.5)
    for k in range(N*N-1):
        # knight_draw(screen, y, x, N, knight)
        valid_moves = []
        for dx, dy in MOVES:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < N and 0 <= new_y < N and not visited[new_x][new_y]:
                count = 0
                for mx, my in MOVES:
                    if 0 <= new_x+mx < N and 0 <= new_y+my < N and not visited[new_x+mx][new_y+my]:
                        count += 1
                valid_moves.append((count, (new_x, new_y)))
        if not valid_moves:
            screen.fill((0, 0, 0))
            fail_text = font.render("Failed to find a knight's tour!!!", True, (255, 0, 0))
            fail_rect = fail_text.get_rect(midleft = (150, 375))
            screen.blit(fail_text, fail_rect)
            pygame.display.flip()
            time.sleep(2.5)
            return False
        valid_moves.sort()
        animate_knight(screen, y, x, valid_moves[0][1][1], valid_moves[0][1][0], N, knight)
        count, (x, y) = valid_moves[0]
        visited[x][y] = True
        draw_knight((x, y))
        pygame.display.update()
        quit()
        time.sleep(0.5)
    # knight_draw(screen, y, x, N, knight)
    screen.fill((0, 0, 0))
    success_text = font.render("Successful Journey of the Knight!!!", True, (0, 255, 255))
    success_rect = success_text.get_rect(midleft = (100, 375))
    screen.blit(success_text, success_rect)
    pygame.display.flip()
    time.sleep(2.5)
    time.sleep(0.5)
    return True
n = True
# Start the game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Draw the game objects
    draw_board()
    knight_tour()

    # Update the display
    pygame.display.update()

# Quit Pygame