import pygame
from icb.hardware.input import Input
from icb.hardware.state import State


class Machine:

    def __init__(self):
        self.state = State.MENU
        self.state.diagnostic = True
        self.rows = 6
        self.columns = 6
        self.left_home = False
        self.right_home = False
        self.left_pos = 0
        self.right_pos = 0
        self.left_max = 400
        self.right_max = 400
        self.inputs = {"left_down": Input(state="low", row=0, column=0, key=pygame.K_a),
                       "left_up": Input(state="low", row=0, column=1, key=pygame.K_s),
                       "right_down": Input(state="low", row=0, column=2, key=pygame.K_d),
                       "right_up": Input(state="low", row=0, column=3, key=pygame.K_f),
                       "left_home": Input(state="low", row=0, column=4, key=pygame.K_g),
                       "right_home": Input(state="low", row=0, column=5, key=pygame.K_h),
                       "start": Input(state="low", row=1, column=0, key=pygame.K_q),
                       "select": Input(state="low", row=1, column=1, key=pygame.K_w),
                       "mode_select": Input(state="low", row=1, column=2, key=pygame.K_m),
                       "hole_1": Input(state="low", row=2, column=0, key=pygame.K_1),
                       "hole_2": Input(state="low", row=2, column=1, key=pygame.K_2),
                       "hole_3": Input(state="low", row=2, column=2, key=pygame.K_3),
                       "hole_4": Input(state="low", row=2, column=3, key=pygame.K_4),
                       "hole_5": Input(state="low", row=2, column=4, key=pygame.K_5),
                       "hole_6": Input(state="low", row=2, column=5, key=pygame.K_6),
                       "hole_7": Input(state="low", row=3, column=0, key=pygame.K_7),
                       "hole_8": Input(state="low", row=3, column=1, key=pygame.K_8),
                       "hole_9": Input(state="low", row=3, column=2, key=pygame.K_9),
                       "lost_ball": Input(state="low", row=3, column=3, key=pygame.K_0),
                       "ball_1": Input(state="low", row=4, column=0, key=pygame.K_z),
                       "ball_2": Input(state="low", row=4, column=1, key=pygame.K_x),
                       "ball_3": Input(state="low", row=4, column=2, key=pygame.K_c)}
        self.newgame = True

    def home(self):
        if self.inputs["left_home"].state == "high":
            self.left_home = True
            self.left_pos = 0
        else:
            self.left_home = False

        if self.inputs["right_home"].state == "high":
            self.right_home = True
            self.right_pos = 0
        else:
            self.right_home = False

        if self.left_home and self.right_home:
            self.state = State.PLAYING
        else:
            self.state = State.HOMING
            if not self.left_home:
                print("Homing left")
            if not self.right_home:
                print("Homing right")
