import json

from icb.screens.page import Page, Item
from icb.utils.colors import Colors


class Highscores(Page):

    def __init__(self, screen, score_file="highscore.json"):
        Page.__init__(self, screen, title="Highscores")
        self.spacing = 30
        self.highscore_file = score_file
        self.highscores = self.load()

    def save(self):
        print("Saving Highscores...")

        with open(self.highscore_file, 'w') as outfile:
            json.dump(self.highscores, outfile, indent=4, sort_keys=True)

    def load(self):
        print("Loading Highscores")
        with open(self.highscore_file) as file:
            return json.load(file)

    def add_score(self, name, score):
        print("Adding score to list")
        self.save()

    def draw(self):
        Page.draw(self)
        current_height = self.font_size+10
        s = sorted(self.highscores, key=lambda k: k["score"], reverse=True)
        highscores = []
        for index, score in enumerate(s):
            highscores.append(Item(self.screen,
                                   text="{0:2d}.{1:>5s}: {2:>20d}".format(index+1, score['name'], score['score']),
                                   item_xpos=10, item_ypos=current_height))
            highscores[index].draw()

            current_height = current_height+self.spacing

