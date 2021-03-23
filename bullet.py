import numpy as np
import config 
from random import randint
from colorama import Fore, Back, Style
from os import system
from time import time
from paddle import Paddle
from board import Board

class Bullet:
    def __init__(self, x, Board, id):
        self.pos = [Board.y_pix - 2, x-1]
        self.id = id
        self.vel = [-1,0]
        self.to_remove = False

    def draw_bullet(self, Board):
        Board.bullet_res[self.pos[0]+1, self.pos[1]] = 0
        Board.bullet_res[self.pos[0], self.pos[1]] = 1
    
    def tick(self, Board):
        if(self.pos[0]-1)==1:
            Board.bullet_res[self.pos[0], self.pos[1]] = 0
            # config.bullet_iter = config.bullet_iter-2
            self.to_remove = True
        elif(Board.res[self.pos[0]-1][self.pos[1]]>0):
            Board.bullet_res[self.pos[0], self.pos[1]] = 0
            for i in config.bricks:
                if Board.res[self.pos[0]-1][self.pos[1]] == i.id:
                    i.hit_brick(Board, self)
                    i.ball_hit = True
            self.to_remove=True
        else:
            self.pos[0] = self.pos[0]-1
            self.draw_bullet(Board)

