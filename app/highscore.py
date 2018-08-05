import pygame

from app.colors import Colors


class Highscores:

    def __init__(self, screen):
        self.fontSize = 30
        self.spacing = 20
        self.screen = screen
        self.highscores = [{"name": "Dan", "score": "1000000"},
                           {"name": "Dan", "score": "90000"},
                           {"name": "Dan", "score": "800"}
                           ]

    def save(self):
        print("Saving Highscores...")

    def load(self, file):
        print("Loading Highscores")

    def add_score(self, name, score):
        print("Adding score to list")
        self.save()

    def draw(self):

        # Set the screen background
        self.screen.fill(Colors.WHITE.value)
        myfont = pygame.font.SysFont('Comic Sans MS', self.fontSize)
        textsurface = myfont.render('Highscores', False, Colors.GREEN.value)
        self.screen.blit(textsurface, (80, 0))
        current_height = self.fontSize
        for score in self.highscores:
            textsurface = myfont.render("%s: %s" % (score['name'], score['score']), False, Colors.BLACK.value)
            self.screen.blit(textsurface, (10, current_height))
            current_height = current_height+self.spacing
