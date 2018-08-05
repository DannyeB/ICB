import pygame

from app.highscore import Highscores
from app.machine import Machine, States
from app.event_handler import handle_events
from app.colors import Colors
from app.diag import Diag
from app.menu import Menu

machine = Machine()
pygame.init()

pygame.font.init()

# Set the width and height of the screen [width, height]
size = (230, 230)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("ICB")

diagnostics = Diag(rows=machine.rows, columns=machine.columns, width=35, height=35, margin=3, screen=screen)
menu = Menu(screen=screen)
highscore = Highscores(screen=screen)
# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


if __name__ == '__main__':
    # -------- Main Program Loop -----------
    while not done:

        done, machine = handle_events(done, machine)
        # Set the screen background
        screen.fill(Colors.BLACK.value)

        if machine.state == States.DIAGNOSTIC:
            diagnostics.draw(machine)
        elif machine.state == States.MENU:
            menu.draw()
        elif machine.state == States.HIGHSCORE:
            highscore.draw()

        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Close the window and quit.
    pygame.quit()