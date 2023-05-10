import pygame
import time

# Initialize Pygame
pygame.init()

# Set up the display window
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set the caption of the window
pygame.display.set_caption("Knight's Tour")

# Define the chessboard parameters
N = 5
SQUARE_SIZE = WIDTH // N

# Define the knight's moves
MOVES = [
    (-2, -1), (-2, 1), (-1, -2), (-1, 2),
    (1, -2), (1, 2), (2, -1), (2, 1)
]

# quitting function
def quit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
# Define a function to draw the chessboard
def draw_board():
    colors = [(255, 255, 255), (0, 0, 0)]
    for i in range(N):
        for j in range(N):
            color = colors[(i + j) % 2]
            rect = pygame.Rect(j * SQUARE_SIZE, i * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
            pygame.draw.rect(screen, color, rect)

# Define a function to draw the knight
def draw_knight(position):
    x, y = position
    rect = pygame.Rect(x * SQUARE_SIZE, y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
    pygame.draw.rect(screen, (255, 0, 0), rect)

# Define the Knight's tour algorithm
def knight_tour():
    visited = [[False for _ in range(N)] for _ in range(N)]
    x, y = 2, 2
    visited[x][y] = True
    draw_knight((x, y))
    pygame.display.update()
    time.sleep(0.5)
    for k in range(N*N-1):
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
            return False
        valid_moves.sort()
        count, (x, y) = valid_moves[0]
        visited[x][y] = True
        draw_knight((x, y))
        pygame.display.update()
        quit()
        time.sleep(0.5)
    return True

# Start the game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Update the game state
    # ...

    # Draw the game objects
    draw_board()
    knight_tour()

    # Update the display
    pygame.display.update()

# Quit Pygame

