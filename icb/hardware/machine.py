import pygame
from icb.hardware.input import Input
from icb.hardware.state import State


class Machine:

    def __init__(self):
        self.state = State.MENU
        self.state.diagnostic = True
        self.rows = 6
        self.columns = 6
        self.inputs = [Input(name="left_down", state="low", row=0, column=0, key=pygame.K_a),
                       Input(name="left_up", state="low", row=0, column=1, key=pygame.K_s),
                       Input(name="right_down", state="low", row=0, column=2, key=pygame.K_d),
                       Input(name="right_up", state="low", row=0, column=3, key=pygame.K_f),
                       Input(name="start", state="low", row=1, column=0, key=pygame.K_q),
                       Input(name="select", state="low", row=1, column=1, key=pygame.K_w),
                       Input(name="mode_select", state="low", row=1, column=2, key=pygame.K_m),
                       Input(name="goal_1", state="low", row=2, column=0, key=pygame.K_1),
                       Input(name="goal_2", state="low", row=2, column=1, key=pygame.K_2),
                       Input(name="goal_3", state="low", row=2, column=2, key=pygame.K_3),
                       Input(name="lost_ball", state="low", row=2, column=2, key=pygame.K_4),
                       Input(name="ball_1", state="low", row=3, column=0, key=pygame.K_z),
                       Input(name="ball_2", state="low", row=3, column=1, key=pygame.K_x),
                       Input(name="ball_3", state="low", row=3, column=2, key=pygame.K_c)]
