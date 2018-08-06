from icb.game.run import Run
from icb.hardware.state import State


class Game:
    def __init__(self):

        self.runs = [Run(name="Level 1", target="goal_1", bonus=10000),
                     Run(name="Level 2", target="goal_2", bonus=1000000),
                     Run(name="Level 3", target="goal_3", bonus=100000000)
                     ]

    def start(self, machine):
        machine.state = State.RUNNING
        self.current_run = self.runs[0]


        return machine
