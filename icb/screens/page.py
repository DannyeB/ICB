import pygame
from icb.utils.colors import Colors
from icb.hardware.state import State

class Page:
    def __init__(self, screen, title="",  title_xpos=80, title_ypos=5, font_color=Colors.BLACK, background_color=Colors.SILVER, font_size=30,
                 font='arial'):
        self.screen = screen
        self.title_ypos = title_ypos
        self.title_xpos = title_xpos
        self.title = title

        self.background_color = background_color.value

        self.font_size = font_size
        self.font = pygame.font.SysFont(font, self.font_size)
        self.font_color = font_color.value

    def draw(self):
        # Set the screen background
        self.screen.fill(self.background_color)
        textsurface = self.font.render(self.title, True, self.font_color)
        self.screen.blit(textsurface, (self.title_xpos, self.title_ypos))

    @staticmethod
    def event_handler(escape, machine):
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                escape = True  # Flag that we are done so we exit this loop
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    escape = True
                elif event.key == pygame.K_m:
                    if machine.state == State.DIAGNOSTIC:
                        print("State: MENU")
                        machine.state = State.MENU
                    elif machine.state == State.MENU:
                        print("State: HIGHSCORE")
                        machine.state = State.HIGHSCORE
                    else:
                        print("State: DIAGNOSTIC")
                        machine.state = State.DIAGNOSTIC

                for inp in machine.inputs:
                    if inp.key == event.key:
                        inp.state = "high"
            elif event.type == pygame.KEYUP:
                for inp in machine.inputs:
                    if inp.key == event.key:
                        inp.state = "low"

        return escape, machine



class Item:
    def __init__(self, screen, text="", item_xpos=0, item_ypos=0, font_color=Colors.BLACK,
                 font_size=30, font='Comic Sans MS', selected=False):
        self.screen = screen
        self.text = text
        self.item_xpos = item_xpos
        self.item_ypos = item_ypos

        self.font_size = font_size
        self.font = pygame.font.SysFont(font, self.font_size)
        self.font_color = font_color.value

        self.selected = selected


    def draw(self):
        self.font.set_bold(self.selected)
        textsurface = self.font.render(self.text, True, self.font_color)
        self.screen.blit(textsurface, (self.item_xpos, self.item_ypos))