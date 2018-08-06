import pygame
from icb.screens.page import Page, Item
from icb.hardware.state import State

class Menu(Page):
    def __init__(self, screen):
        Page.__init__(self, screen, title='Menu')
        self.menu_items = [Item(screen, text="Play", item_xpos=10, item_ypos=30, selected=True),
                           Item(screen, text="Highscores", item_xpos=10, item_ypos=55),
                           Item(screen, text="Diagnostics", item_xpos=10, item_ypos=80)
                           ]

    def draw(self):
        Page.draw(self)
        for item in self.menu_items:
            item.draw()


    # @staticmethod
    # def event_handler(escape, machine):
    #     for event in pygame.event.get():  # User did something
    #         if event.type == pygame.QUIT:  # If user clicked close
    #             escape = True  # Flag that we are done so we exit this loop
    #         elif event.type == pygame.KEYDOWN:
    #             if event.key == pygame.K_ESCAPE:
    #                 escape = True
    #             else:
    #                 for inp in machine.inputs:
    #                     if inp.key == event.key:
    #                         inp.state = "high"
    #
    #
    #     return escape, machine
