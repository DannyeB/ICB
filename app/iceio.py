import pygame

class IO:

    def __init__(self):
        self.rows = 6
        self.columns = 6
        self.inputs = [Input(name="left_down", state="low", row=0, column=0, key=pygame.K_a),
                       Input(name="left_up", state="low", row=0, column=1, key=pygame.K_s),
                       Input(name="right_down", state="low", row=0, column=2, key=pygame.K_d),
                       Input(name="right_up", state="low", row=0, column=3, key=pygame.K_f),
                       Input(name="start", state="low", row=1, column=0, key=pygame.K_q),
                       Input(name="select", state="low", row=1, column=1, key=pygame.K_w),
                       Input(name="goal_1", state="low", row=2, column=0, key=pygame.K_1),
                       Input(name="goal_2", state="low", row=2, column=1, key=pygame.K_2),
                       Input(name="goal_3", state="low", row=2, column=2, key=pygame.K_3),
                       Input(name="ball_1", state="low", row=3, column=0, key=pygame.K_z),
                       Input(name="ball_2", state="low", row=3, column=1, key=pygame.K_x),
                       Input(name="ball_3", state="low", row=3, column=2, key=pygame.K_c)]


class Input:
    def __init__(self, name, state, row, column, key):
        self.name = name
        self.state = state
        self.row = row
        self.column = column
        self.key = key
