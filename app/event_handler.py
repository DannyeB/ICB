import pygame
from app.machine import States


def handle_events(done, machine):
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
            elif event.key == pygame.K_m:
                if machine.state == States.DIAGNOSTIC:
                    print("State: MENU")
                    machine.state = States.MENU
                elif machine.state == States.MENU:
                    print("State: HIGHSCORE")
                    machine.state = States.HIGHSCORE
                else:
                    print("State: DIAGNOSTIC")
                    machine.state = States.DIAGNOSTIC

            for inp in machine.inputs:
                if inp.key == event.key:
                    inp.state = "high"
        elif event.type == pygame.KEYUP:
            for inp in machine.inputs:
                if inp.key == event.key:
                    inp.state = "low"

    return done, machine
