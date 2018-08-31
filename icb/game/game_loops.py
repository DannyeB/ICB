from icb.game.level import Level
from icb.hardware.state import State
from icb.game.difficulty import Difficulty
from pygame.time import get_ticks

class Game:
    def __init__(self, difficulty=Difficulty.EASY):

        self.runs = [Level(name="Level 1", target="goal_1", time_limit=120, target_time=30, difficulty=difficulty),
                     Level(name="Level 2", target="goal_2", time_limit=120, target_time=60, difficulty=difficulty),
                     Level(name="Level 3", target="goal_3", time_limit=120, target_time=120, difficulty=difficulty)
                     ]

        self.current_level = 0
        self.current_run = self.runs[self.current_level]
        self.left_home = False
        self.right_home = False
        self.balls = self.current_run.balls
        self.score = 0
        self.state = State.HOMING
        self.start_time = get_ticks()
        self.time_seconds = 0

    def update_game_loop(self):
        self.time_seconds = int((get_ticks() - self.start_time)/1000)
        if self.current_run.bonus > 0:
            self.current_run.bonus = self.current_run.bonus-self.current_run.difficulty.value

        else:
            self.current_run.bonus = 0

        if self.balls <= 0:
            self.state = State.GAME_OVER

    def next_level(self):
        self.score += self.current_run.bonus
        self.score += self.balls * self.current_run.difficulty.value
        self.current_level = self.current_level+1
        if self.current_level < len(self.runs):
            print("Next Level!")
            self.state = State.HOMING
            self.current_run = self.runs[self.current_level]
            self.start_time = get_ticks()
            self.time_seconds = 0
        else:
            print('Congratulations game complete')
            print("Your Score: %s" % self.score)
            self.state = State.GAME_OVER

    def update_home_loop(self):
        if self.left_home and self.right_home:
            self.state = State.PLAYING
        else:
            self.state = State.HOMING
            if not self.left_home:
                print("Homing left")
            if not self.right_home:
                print("Homing right")