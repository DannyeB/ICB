from icb.game.level import Level
from icb.hardware.state import State
from icb.game.difficulty import Difficulty
from pygame.time import get_ticks

class Game:
    def __init__(self, difficulty=Difficulty.EASY, balls=5):

        self.levels = Level.load_levels(difficulty=difficulty)
        self.current_level_number = 0
        self.current_level = self.levels[self.current_level_number]
        self.left_home = False
        self.right_home = False
        self.left_pos = 0
        self.right_pos = 0
        self.left_max = 400
        self.right_max = 400
        self.move_distance = 5
        self.balls = balls
        self.score = 0
        self.state = State.HOMING
        self.start_time = get_ticks()
        self.time_seconds = 0

    def update_game_loop(self):
        self.time_seconds = int((get_ticks() - self.start_time)/1000)
        if self.current_level.bonus > 0:
            self.current_level.bonus = self.current_level.bonus - self.current_level.difficulty.value

        else:
            self.current_level.bonus = 0

        if self.balls <= 0:
            self.state = State.GAME_OVER

    def next_level(self):
        self.score += self.current_level.bonus
        self.score += self.balls * self.current_level.difficulty.value
        self.current_level_number = self.current_level_number+1
        if self.current_level_number < len(self.levels):
            print("Next Level!")
            self.state = State.HOMING
            self.current_level = self.levels[self.current_level_number]
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