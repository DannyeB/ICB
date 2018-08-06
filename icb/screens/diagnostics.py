import pygame
from icb.utils.colors import Colors
from icb.screens.page import Page


class Diagnostics(Page):
    def __init__(self, rows, columns, width, height, margin, screen):
        Page.__init__(self, screen=screen, title='Diagnostics')
        self.rows = rows
        self.columns = columns
        self.width = width
        self.height = height
        self.margin = margin

        self.grid_top = 50
        self.grid_left = 10

    def draw(self, machine):
        Page.draw(self)
        for row in range(self.rows):
            for column in range(self.columns):
                color = Colors.WHITE.value
                for inp in machine.inputs:
                    if inp.row == row and inp.column == column and inp.state == "high":
                        color = Colors.GREEN.value
                pygame.draw.rect(self.screen,
                                 color,
                                 [(self.margin + self.width) * column + self.margin + self.grid_left,
                                  (self.margin + self.height) * row + self.margin + self.grid_top,
                                  self.width,
                                  self.height])
