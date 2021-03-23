import numpy as np
import config 
from random import randint
from colorama import Fore, Back, Style
from os import system
from time import time
from paddle import Paddle
from board import Board

class Bomb:
    def __init__(self, y,x):
        self.pos = [y, x]
        self.to_remove = False
    
    def draw_bomb(self, Board):
        Board.bomb_res[self.pos[0]-1][self.pos[1]]=0
        Board.bomb_res[self.pos[0]][self.pos[1]]=1

    def bomb_tick(self,Board):
        if(self.pos[0]+1)==Board.y_pix:
            Board.bomb_res[self.pos[0], self.pos[1]] = 0
            self.to_remove = True
        elif(self.pos[0]+1 == Board.y_pix-1 and Board.res[self.pos[0]+1][self.pos[1]] == -2):
            config.life_end= True
            self.to_remove=True
        else:
            self.pos[0] = self.pos[0]+1
            self.draw_bomb(Board)