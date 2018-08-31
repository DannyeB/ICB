import json

from icb.game.difficulty import Difficulty


class Level:
    def __init__(self, name, target, time_limit, target_time, balls=5, bonus_multiplier=100, difficulty=Difficulty.EASY):
        self.difficulty = difficulty
        self.name = name
        self.balls = balls
        self.target = target
        self.time_limit = time_limit
        self.target_time = target_time
        self.bonus = bonus_multiplier * target_time

    @staticmethod
    def load_level(level_obj, difficulty):

        print(level_obj)
        level = Level(name=level_obj['name'], balls=level_obj['balls'], target=level_obj['target'],
                      target_time=level_obj['target_time'], time_limit=level_obj['time_limit'], difficulty=difficulty)
        return level

    @staticmethod
    def load_levels(difficulty=Difficulty.EASY, level_file='levels.json'):
        levels = []
        with open(level_file) as file:
            for level in json.load(file):
                levels.append(Level.load_level(level, difficulty))

        return levels
