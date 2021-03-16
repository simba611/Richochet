import numpy as np
import config 
from random import randint

class Ball:
    def __init__(self, Board, Paddle):
        # self.pos = [Board.y_pix-2, int(Paddle.pos + Paddle.length/2)]
        self.pos = [Board.y_pix-2, randint(int(Paddle.pos), int(Paddle.pos+Paddle.length))]
        self.vel = [-1,  -1*(int(Paddle.pos + Paddle.length/2) - self.pos[1])]
        # self.vel = [-1,  0]
        self.next_pos = [self.pos[0]-self.vel[0], self.pos[1]+self.vel[1]]
        self.prev_pos = [self.pos[0], self.pos[1]]
        self.angle = self.vel[1]/self.vel[0]
        self.ini_pos = [self.pos[0], self.pos[1]]
        self.imm_next_pos = [0, 0]
        self.paddle_attach = True
        if self.vel[1]>4:
            self.vel[1] = 4
        if self.vel[1] < -4:
            self.vel[1] = -4

    def draw_ball(self, Board):
        Board.res[self.ini_pos[0]][self.ini_pos[1]] = 0
        Board.res[self.pos[0]][self.pos[1]] = -3

    def handleXCollision(self, Board, Paddle):
        if( Board.res[self.pos[0]][self.imm_next_pos[1]] == -2 or Board.res[self.pos[0]][self.imm_next_pos[1]] > 0) or self.imm_next_pos[1]==-1 or self.imm_next_pos[1] == Board.x_pix:
            if (not Board.res[self.pos[0]][self.imm_next_pos[1]] > 0 or not config.through_ball):
                self.draw_ball(Board)
                self.vel[1] = -1*self.vel[1]
                self.next_pos = [self.pos[0]-self.vel[0], self.pos[1]+self.vel[1]]
                self.prev_pos = [self.pos[0], self.pos[1]]
                self.ini_pos = [self.pos[0], self.pos[1]]
                self.angle = self.vel[1]/self.vel[0]
        if(Board.res[self.pos[0]][self.imm_next_pos[1]] > 0 ):
            for i in config.bricks:
                if Board.res[self.pos[0]][self.imm_next_pos[1]] == i.id:
                    # if i.strength !=4:
                    if not config.through_ball:
                        i.hit_brick(Board)
                    else:
                        i.destroy_brick(Board)
        else:
            # print("a")
            self.prev_pos[0] = self.pos[0]
            self.prev_pos[1] = self.pos[1]
            if self.vel[1] > 0:
                self.pos[1] = self.pos[1] + 1
            else:
                self.pos[1] = self.pos[1] - 1


    def handleYCollision(self, Board, Paddle):
        # print("b")
        if self.imm_next_pos[0] == Board.y_pix-1 or (Board.res[self.imm_next_pos[0]][self.pos[1]] > 0 or Board.res[self.imm_next_pos[0]][self.pos[1]] == -2) or self.imm_next_pos[0] == -1 :
            if Board.res[self.imm_next_pos[0]][self.pos[1]] == -2 and self.imm_next_pos[0]!= -1:
                if(self.vel[1]!=0):
                    self.vel[1] = (self.vel[1]/abs(self.vel[1]))*abs(int(Paddle.pos + Paddle.length/2) - self.pos[1])
                else:
                    self.vel[1] = -1*(int(Paddle.pos + Paddle.length/2) - self.pos[1])
                if self.vel[1]>4:
                    self.vel[1] = 4
                if self.vel[1]< -4:
                    self.vel[1] = -4
            elif self.imm_next_pos[0] == Board.y_pix - 1 and Board.res[self.imm_next_pos[0]][self.pos[1]] != -2:
                config.lives = config.lives - 1
            if (not Board.res[self.imm_next_pos[0]][self.pos[1]] > 0) or not config.through_ball:
                self.draw_ball(Board)
                self.vel[0] = -1*self.vel[0]
                self.next_pos = [self.pos[0]-self.vel[0], self.pos[1]+self.vel[1]]
                self.prev_pos = [self.pos[0], self.pos[1]]
                self.ini_pos = [self.pos[0], self.pos[1]]
                self.angle = self.vel[1]/self.vel[0]
        if Board.res[self.imm_next_pos[0]][self.pos[1]] > 0:
            for i in config.bricks:
                if Board.res[self.imm_next_pos[0]][self.pos[1]] == i.id:
                    if not config.through_ball:
                        i.hit_brick(Board)
                    else:
                        i.destroy_brick(Board)
        else:
            self.prev_pos[0] = self.pos[0]
            self.prev_pos[1] = self.pos[1]
            if self.vel[0] > 0:
                self.pos[0] = self.pos[0] - 1
            else:
                self.pos[0] = self.pos[0] + 1

    def mov_ball(self, Board, Paddle):
        if not (self.paddle_attach == True and Board.res[self.pos[0]+1][self.pos[1]] == -2):
            if self.vel[1] == 0:
                self.prev_pos[0] = self.pos[0]
                self.prev_pos[1] = self.pos[1]
                if self.vel[0] > 0:
                    self.imm_next_pos[0] = self.pos[0] - 1
                else:
                    self.imm_next_pos[0] = self.pos[0] + 1
                self.handleYCollision(Board, Paddle)
            else:
                if (self.next_pos[0]-self.pos[0]) == 0 or abs((self.next_pos[1]-self.pos[1])/(self.next_pos[0]-self.pos[0])) >= abs(self.angle):
                # if (self.next_pos[0]-self.pos[0]) != 0 and self.pos[1] - self.ini_pos[1] < int((self.next_pos[1]-self.ini_pos[1])/2):
                    if self.vel[1] > 0:
                        self.imm_next_pos[1] = self.pos[1]+1
                    else:
                        self.imm_next_pos[1] = self.pos[1]-1
                    self.handleXCollision(Board, Paddle)
                else:
                    if self.vel[0] > 0:
                        self.imm_next_pos[0] = self.pos[0] - 1
                    else:
                        self.imm_next_pos[0] = self.pos[0] + 1
                    self.handleYCollision(Board, Paddle)


            if self.next_pos[0] == self.pos[0] and self.next_pos[1] == self.pos[1]:
                self.draw_ball(Board)
                self.next_pos = [self.pos[0]-self.vel[0], self.pos[1]+self.vel[1]]
                self.ini_pos = [self.pos[0], self.pos[1]]
                self.angle = self.vel[1]/self.vel[0]