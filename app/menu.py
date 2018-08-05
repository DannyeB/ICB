import pygame
from app.colors import Colors


class Menu:
    def __init__(self, screen):
        self.screen = screen

    def draw(self):
        # Set the screen background
        self.screen.fill(Colors.WHITE.value)
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        textsurface = myfont.render('Menu', False, Colors.GREEN.value)
        self.screen.blit(textsurface, (80, 0))
