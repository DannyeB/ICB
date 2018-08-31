from icb.game.difficulty import Difficulty


class Run:
    def __init__(self, name, target, time_limit, target_time, balls=5, bonus_multiplier=100, difficulty=Difficulty.EASY):
        self.difficulty = difficulty
        self.name = name
        self.balls = balls
        self.target = target
        self.time_limit = time_limit
        self.target_time = target_time
        self.bonus = bonus_multiplier * target_time
