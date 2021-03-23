import numpy as np
import config 
from random import randint
from colorama import Fore, Back, Style
from os import system
from time import time
from paddle import Paddle
from board import Board
from brick import Brick

class Boss:
    def __init__(self, x):
        self.health = 10
        self.pos = x
        self.length = config.boss_length
    
    def draw_boss(self, Board):
        for j in range(len(Board.boss_res[0])):
            Board.boss_res[int(Board.y_pix/10) - 2][j] = 0
        for j in range(self.pos, self.pos+self.length):
            Board.boss_res[int(Board.y_pix/10) - 2][j] = 1
    
    def hit_boss(self, Board):
        self.health=self.health-1
        config.boss_health = self.health
        if self.health == 0:
            for hh in range(Board.y_pix + 4):
                for jj in range(Board.x_pix):
                    print(" ", end = "")
                print("")
            for hh in range(Board.y_pix + 4):
                print("\033[F", end = "")
            print("Game Over")
            print(Back.RESET+Fore.RESET+"Lives: " + str(config.lives))
            # print(Back.RESET+Fore.RESET+"Time: " + str(int((int(time()-config.start_time))/60))+ (":" if (len(str((int(time()-config.start_time))%60))==2) else ":0")+ str((int(time()-config.start_time))%60))
            print(Back.RESET+Fore.RESET+"Score: " + str(config.score))
            system("stty echo")
            quit()
        if self.health == 9 or self.health==6:
            # count = 1
            ii = 0
            while ii<len(config.bricks):
                if config.bricks[ii].strength!=4 and config.bricks[ii].pos[0]==(Board.y_pix/10)-1:
                    config.bricks.remove(config.bricks[ii])
                    ii = ii - 1
                ii = ii+1
            # config.bricks.clear()
            plpl=1
            if self.health == 8:
                plpl=2 
            for i in range(Board.y_pix-int(Board.y_pix/2)):
                if i == (Board.y_pix/10)-1:
                    for j in range(((int(int(Board.x_pix/2)/config.brick_len)))):
                        # if j != 0:
                            # if(randint(0,4)==1):
                            #     rand = randint(1,4)
                            #     if rand == 4:
                            #         if randint(0,1) == 1:
                            #             rand = randint(1,3)
                            #     if rand !=4:
                            #         config.no_bricks = config.no_bricks+2
                            config.bricks.append(Brick(config.brick_len*j,i,len(config.bricks)+3000*plpl, randint(1,3)))
                            config.bricks.append(Brick(Board.x_pix - config.brick_len -config.brick_len*j,i,len(config.bricks)+3000*plpl, randint(1,3)))
                            # count = count + 2
            for i in config.bricks:
                if i.strength!=4:
                    i.createBrick(Board)           


    