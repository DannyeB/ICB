import pygame
from app.iceio import IO

machine = IO()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

# Set the width and height of the screen [width, height]
size = (230, 230)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("ICB")

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 35
HEIGHT = 35
# This sets the margin between each cell
MARGIN = 3

# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
for row in range(machine.rows):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(machine.columns):
        grid[row].append(0)  # Append a cell

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.KEYDOWN:
            for inp in machine.inputs:
                if inp.key == event.key:
                    inp.state = "high"
        elif event.type == pygame.KEYUP:
            for inp in machine.inputs:
                if inp.key == event.key:
                    inp.state = "low"

    # Set the screen background
    screen.fill(BLACK)

    # Draw the grid
    for row in range(machine.rows):
        for column in range(machine.columns):
            color = WHITE
            for inp in machine.inputs:
                if inp.row == row and inp.column == column and inp.state == "high":
                    color = GREEN
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])

    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# Close the window and quit.
pygame.quit()