import pygame
from icb.utils.colors import Colors
from icb.hardware.state import State

class Page:
    def __init__(self, screen, machine, title="",  title_xpos=80, title_ypos=5, font_color=Colors.BLACK,
                 background_color=Colors.SILVER, font_size=30,font='arial',
                 defaut_item_x=10, defaut_item_first_y=55, default_item_y_increment=30):

        self.machine = machine
        self.screen = screen
        self.title_ypos = title_ypos
        self.title_xpos = title_xpos
        self.title = title

        self.selected = 0
        self.menu_items = []
        self.background_color = background_color.value

        self.font_size = font_size
        self.font = pygame.font.SysFont(font, self.font_size)
        self.font_color = font_color.value

        self.defaut_item_x = defaut_item_x
        self.defaut_item_first_y = defaut_item_first_y
        self.default_item_y_increment = default_item_y_increment

    def draw(self):
        # Set the screen background
        self.screen.fill(self.background_color)
        textsurface = self.font.render(self.title, True, self.font_color)
        self.screen.blit(textsurface, (self.title_xpos, self.title_ypos))

    def add_menu_item(self, text, machine_state=None, xpos=None, ypos=None, y_increment=None, font_color=Colors.BLACK,
                      font_size=30, font='arial', selected=False):
        if xpos is None:
            xpos = self.defaut_item_x
        if y_increment is None:
            y_increment = self.default_item_y_increment
        if ypos is None:
            if len(self.menu_items) > 0:
                ypos = self.defaut_item_first_y + (len(self.menu_items) * y_increment)
            else:
                ypos = self.defaut_item_first_y

        self.menu_items.append(MenuItem(self.screen, machine_state, text, xpos, ypos, font_color=font_color,
                                        font_size=font_size, font=font, selected=selected))

    def menu_down(self):
        if len(self.menu_items) > 0:
            self.menu_items[self.selected].selected = False
            if self.selected < (len(self.menu_items)-1):
                self.selected = self.selected+1
            else:
                self.selected = 0
            self.menu_items[self.selected].selected = True

    def menu_up(self):
        if len(self.menu_items) > 0:
            self.menu_items[self.selected].selected = False
            if self.selected > 0:
                self.selected = self.selected-1
            else:
                self.selected = len(self.menu_items)-1
            self.menu_items[self.selected].selected = True

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
                        machine.state = State.HIGH_SCORE
                    else:
                        print("State: DIAGNOSTIC")
                        machine.state = State.DIAGNOSTIC

                for name, inp in machine.inputs.items():
                    if inp.key == event.key:
                        inp.state = "high"
            elif event.type == pygame.KEYUP:
                for name, inp in machine.inputs.items():
                    if inp.key == event.key:
                        inp.state = "low"

        return escape, machine


class MenuItem:
    def __init__(self, screen, machine_state=None, text="", item_xpos=0, item_ypos=0, font_color=Colors.BLACK,
                 font_size=30, font='arial', selected=False):
        self.screen = screen
        self.text = text
        self.item_xpos = item_xpos
        self.item_ypos = item_ypos

        self.font_size = font_size
        self.font = pygame.font.SysFont(font, self.font_size)
        self.font_color = font_color.value

        self.selected = selected
        self.machine_state = machine_state

    def draw(self):
        self.font.set_bold(self.selected)
        textsurface = self.font.render(self.text, True, self.font_color)
        self.screen.blit(textsurface, (self.item_xpos, self.item_ypos))