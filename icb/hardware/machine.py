import pygame
from icb.hardware.input import Input
from icb.hardware.state import State


class Machine:

    def __init__(self):
        self.state = State.MENU
        self.state.diagnostic = True
        self.rows = 6
        self.columns = 6
        self.inputs = {"left_down": Input(state="low", row=0, column=0, key=pygame.K_a),
                       "left_up": Input(state="low", row=0, column=1, key=pygame.K_s),
                       "right_down": Input(state="low", row=0, column=2, key=pygame.K_d),
                       "right_up": Input(state="low", row=0, column=3, key=pygame.K_f),
                       "left_home": Input(state="low", row=0, column=4, key=pygame.K_g),
                       "right_home": Input(state="low", row=0, column=5, key=pygame.K_h),
                       "start": Input(state="low", row=1, column=0, key=pygame.K_q),
                       "select": Input(state="low", row=1, column=1, key=pygame.K_w),
                       "mode_select": Input(state="low", row=1, column=2, key=pygame.K_m),
                       "goal_1": Input(state="low", row=2, column=0, key=pygame.K_1),
                       "goal_2": Input(state="low", row=2, column=1, key=pygame.K_2),
                       "goal_3": Input(state="low", row=2, column=2, key=pygame.K_3),
                       "lost_ball": Input(state="low", row=2, column=2, key=pygame.K_4),
                       "ball_1": Input(state="low", row=3, column=0, key=pygame.K_z),
                       "ball_2": Input(state="low", row=3, column=1, key=pygame.K_x),
                       "ball_3": Input(state="low", row=3, column=2, key=pygame.K_c)}
