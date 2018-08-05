import pygame
from app.colors import Colors


class Diag:
    def __init__(self, rows, columns, width, height, margin, screen):
        self.rows = rows
        self.columns = columns
        self.width = width
        self.height = height
        self.margin = margin

        self.screen = screen

        # Create a 2 dimensional array. A two dimensional
        # array is simply a list of lists.
        self.grid = []
        for row in range(self.rows):
            # Add an empty array that will hold each cell
            # in this row
            self.grid.append([])
            for column in range(self.columns):
                self.grid[row].append(0)  # Append a cell

    def draw(self, machine):
        # Set the screen background
        self.screen.fill(Colors.BLACK.value)
        # Draw the grid
        for row in range(self.rows):
            for column in range(self.columns):
                color = Colors.WHITE.value
                for inp in machine.inputs:
                    if inp.row == row and inp.column == column and inp.state == "high":
                        color = Colors.GREEN.value
                pygame.draw.rect(self.screen,
                                 color,
                                 [(self.margin + self.width) * column + self.margin,
                                  (self.margin + self.height) * row + self.margin,
                                  self.width,
                                  self.height])
