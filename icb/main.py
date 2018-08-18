import pygame

from icb.screens.highscore import Highscores
from icb.hardware.machine import Machine
from icb.hardware.state import State
from icb.screens.diagnostics import Diagnostics
from icb.screens.menu import Menu

machine = Machine()
pygame.init()

pygame.font.init()

# Set the width and height of the screen [width, height]
size = (272, 480)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("ICB")

diagnostics = Diagnostics(screen=screen, machine=machine,
                          rows=machine.rows, columns=machine.columns, width=35, height=35, margin=3)
menu = Menu(screen=screen, machine=machine)
highscore = Highscores(screen=screen, machine=machine)
# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


if __name__ == '__main__':
    # -------- Main Program Loop -----------
    while not done:
        if machine.state == State.DIAGNOSTIC:
            done, machine = diagnostics.event_handler(done, machine)
            diagnostics.draw(machine)
        elif machine.state == State.MENU:
            done, machine = menu.event_handler(done, machine)
            menu.draw()
        elif machine.state == State.HIGH_SCORE:
            done, machine = highscore.event_handler(done, machine)
            highscore.draw()
        else:
            machine.state = State.MENU

        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Close the window and quit.
    pygame.quit()