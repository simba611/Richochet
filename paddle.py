import numpy as np
import config
from colorama import Fore, Back, Style
from os import system
from time import time

class Paddle:
    def __init__(self, length, Board):
        self.length = length
        self.pos=int(Board.x_pix/2 - length/2)

    def draw_paddle(self, Board):
        for i in range(Board.x_pix):
            Board.res[Board.y_pix-1][i] = 0
        for i in range(self.length):
            Board.res[Board.y_pix-1][self.pos+i] = -2

    def mov_paddle(self, dir, Board, Ball, Boss):
        if dir == "a":
            if config.level==2:
                Boss.pos = self.pos + int(self.length/2)-int(Boss.length/2)
                if Boss.pos <0:
                    Boss.pos = 0
                if Boss.pos+Boss.length>Board.x_pix-1:
                    Boss.pos = Board.x_pix-Boss.length
            if self.pos != 0:
                if (Ball.paddle_attach == True and Board.res[Ball.pos[0]+1][Ball.pos[1]] == -2):
                    if config.brick_fall_paddle_touch == True:
                        if config.brick_fall==True:
                            Board.clearBoard()
                            for i in config.bricks:
                                i.pos[0] = i.pos[0]+1
                                i.createBrick(Board)
                                if i.pos[0] == Board.y_pix-2:
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
                            Board.print_board()
                            config.brick_fall_paddle_touch = False
                    Ball.next_pos[1] = Ball.next_pos[1] - 1
                    Ball.pos[1] = Ball.pos[1] - 1
                    Ball.draw_ball(Board)
                    Ball.ini_pos[0] = Board.y_pix-2
                    Ball.ini_pos[1] = Ball.pos[1]
                self.pos = self.pos-1
        elif dir == "d":
            if config.level==2:
                Boss.pos = self.pos + int(self.length/2)-int(Boss.length/2)
                if Boss.pos <0:
                    Boss.pos = 0
                if Boss.pos+Boss.length>Board.x_pix-1:
                    Boss.pos = Board.x_pix-Boss.length
            if self.pos + self.length != Board.x_pix:
                if (Ball.paddle_attach == True and Board.res[Ball.pos[0]+1][Ball.pos[1]] == -2):
                    if config.brick_fall_paddle_touch == True:
                        if config.brick_fall==True:
                            Board.clearBoard()
                            for i in config.bricks:
                                i.pos[0] = i.pos[0]+1
                                i.createBrick(Board)
                                if i.pos[0] == Board.y_pix-2:
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
                            Board.print_board()
                            config.brick_fall_paddle_touch = False
                    Ball.next_pos[1] = Ball.next_pos[1] + 1
                    Ball.pos[1] = Ball.pos[1] + 1
                    Ball.draw_ball(Board)
                    Ball.ini_pos[0] = Board.y_pix-2
                    Ball.ini_pos[1] = Ball.pos[1]
                self.pos = self.pos + 1
        else:
            # print("yes", end="")
            if config.level==2:
                Boss.pos = self.pos + int(self.length/2)-int(Boss.length/2)
                if Boss.pos <0:
                    Boss.pos = 0
                if Boss.pos+Boss.length>Board.x_pix-1:
                    Boss.pos = Board.x_pix-Boss.length
            if (Ball.paddle_attach == True and Board.res[Ball.pos[0]+1][Ball.pos[1]] == -2):
                if config.brick_fall_paddle_touch == True:
                    if config.brick_fall==True:
                            Board.clearBoard()
                            for i in config.bricks:
                                i.pos[0] = i.pos[0]+1
                                i.createBrick(Board)
                                if i.pos[0] == Board.y_pix-2:
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
                            Board.print_board()
                            config.brick_fall_paddle_touch = False
                Ball.draw_ball(Board)
                Ball.ini_pos[0] = Board.y_pix-2
                Ball.ini_pos[1] = Ball.pos[1] 
        # Ball.dist_paddle = Ball.pos[1] - self.pos
        self.draw_paddle(Board)
