import numpy as np
import config 
from random import randint
from time import time, sleep

class PowerUp:
    def __init__(self, Brick, Board, id, power=2):
        self.x = Brick.pos[1]
        self.y = Brick.pos[0]
        self.id = id
        self.vel = 1
        self.power = power
        # self.power = randint(1,6)
        self.start = 0

    def activate(self, Ball, Paddle, Board):
        self.start = time()
        config.active_powerup.append(self)
        # print("i got activated")
        # sleep(5)
        # if self.power == 5:
        #     config.paddle_attach=True
        #     Ball.paddle_attach = True
        if self.power == 1:
            config.no_len_plus = config.no_len_plus + 1
        if self.power == 2:
            config.no_len_minus = config.no_len_minus + 1


    def draw_powerup(self, Board):
        Board.power_res[self.y-1][self.x]=0
        Board.power_res[self.y][self.x] = self.id

    def fall(self, Paddle, Board, Ball):
        if self.y == Board.y_pix - 1 and self.start == 0:
            for pu in config.fall_powerup:
                if pu.id == self.id:
                    self.id = 0
                    config.fall_powerup.remove(pu)
        elif Board.res[self.y+1][self.x] == -2:
            config.fall_powerup.remove(self)
            self.id = 0
            self.activate(Ball, Paddle, Board)
        else:
            self.y = self.y+1
        self.draw_powerup(Board)
        




