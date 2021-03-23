import numpy as np
import config 
from random import randint
from time import time, sleep

class PowerUp:
    def __init__(self, Brick, Board, id, power, Ball):
        self.x = Brick.pos[1]
        self.y = Brick.pos[0]
        self.id = id
        self.vel = [-1,Ball.vel[1]]
        self.power = power
        self.up = 4
        self.mov = abs(self.vel[0])
        self.mov_counter = 0
        # self.power = randint(1,6)
        self.start = 0
        self. prev_pos = [self.x, self.y]
        self.ball_dir = int(Ball.vel[0]/abs(Ball.vel[0]))


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
        Board.power_res[self.prev_pos[0]][self.prev_pos[1]]=0
        # Board.power_res[self.y-int(self.vel[0])][self.x-int(self.vel[1])]=0
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
        else:                                        # movement of powerup here
            self.prev_pos[0] = self.y
            self.prev_pos[1] = self.x 
            if self.mov_counter==0:
                if self.ball_dir == -1:
                    if(self.up>0):
                        self.up = self.up-1
                    if self.up == 0:
                        self.vel[0] = self.vel[0]*-1
                        self.up = self.up - 1
                    self.y = self.y + self.vel[0]
                else: 
                    self.y = self.y+1
                self.x = int(self.x + int(self.vel[1]))
                if self.x > Board.x_pix - 1 or self.x < 0:
                    self.x = int(self.x - int(self.vel[1]))
                    self.vel[1] = self.vel[1]*-1
            self.mov_counter = int(int(self.mov_counter+1)%self.mov)
            # if self.x > Board.
        self.draw_powerup(Board)
        




