import pygame
import time
import random

# Initialize pygame
pygame.init()

# Set screen dimensions
width = 600
height = 400

# Create game window
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Madhab's Snake Game")

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Set snake block size and speed
block_size = 20
snake_speed = 10

# Font for text
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Function to display the current score
def your_score(score):
    value = score_font.render("Your Score: " + str(score), True, black)
    win.blit(value, [0, 0])

# Function to draw the snake
def draw_snake(block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(win, green, [x[0], x[1], block_size, block_size])

# Message function to show text on screen
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    win.blit(mesg, [width / 6, height / 3])

# Main game loop
def gameLoop():
    game_over = False
    game_close = False

    # Initial position of the snake
    x1 = width / 2
    y1 = height / 2

    # Change in position
    x1_change = 0
    y1_change = 0

    # Snake body list
    snake_list = []
    length_of_snake = 1

    # Random food position
    foodx = round(random.randrange(0, width - block_size) / 20.0) * 20.0
    foody = round(random.randrange(0, height - block_size) / 20.0) * 20.0

    clock = pygame.time.Clock()

    # Main loop
    while not game_over:

        # Display message and restart/quit if game over
        while game_close:
            win.fill(blue)
            message("You Lost! Press P to Play Again or Q to Quit", red)
            your_score(length_of_snake - 1)
            pygame.display.update()

            # Event handler for restart or quit
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_p:
                        gameLoop()

        # Handle events (key press)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0

        # Check for wall collision
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        # Update snake position
        x1 += x1_change
        y1 += y1_change
        win.fill(blue)  # Fill background
        pygame.draw.rect(win, red, [foodx, foody, block_size, block_size])  # Draw food

        # Update snake head and body
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Check for self collision
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        # Draw snake and score
        draw_snake(block_size, snake_list)
        your_score(length_of_snake - 1)

        pygame.display.update()

        # Check if snake eats food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - block_size) / 20.0) * 20.0
            foody = round(random.randrange(0, height - block_size) / 20.0) * 20.0
            length_of_snake += 1

        # Control speed
        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Run the game
gameLoop()
