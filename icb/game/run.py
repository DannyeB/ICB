from icb.game.difficulty import Difficulty


class Run:
    def __init__(self, name, target, bonus, difficulty=Difficulty.EASY):
        self.difficulty = difficulty
        self.name = name
        self.target = target
        self.bonus = bonus
