import numpy as np
from colorama import Fore, Back, Style
import config
from time import process_time, time

class Board:
    def __init__(self, x_pix, y_pix):
        self.x_pix=x_pix
        self.y_pix=y_pix
        self.lives = 3
        self.res = np.full((y_pix, x_pix+1), 0)
        self.power_res = np.full((y_pix, x_pix+1), 0)
        self.bullet_res = np.full((y_pix, x_pix+1), 0)
        self.boss_res = np.full((y_pix, x_pix+1), 0)
        self.bomb_res = np.full((y_pix, x_pix+1), 0)
        self.test=1
        for i, val in enumerate(self.res):
            self.res[i][x_pix]=-1
        for i, val in enumerate(self.power_res):
            self.power_res[i][x_pix]=-1
        for i, val in enumerate(self.bullet_res):
            self.bullet_res[i][x_pix]=-1
        for i, val in enumerate(self.boss_res):
            self.boss_res[i][x_pix]=-1
        for i, val in enumerate(self.bomb_res):
            self.bomb_res[i][x_pix]=-1

    def clearBoard(self):
        for i,rows in enumerate(self.res):
            for j,cols in enumerate(rows):
                if self.res[i][j] >0:
                    self.res[i][j]=0

    def print_board(self):
        for i in range(self.x_pix+1):
            # print(Back.RESET + "_", end="")
            if i == self.x_pix:
                print("")
        for i, rows in enumerate(self.res):
            # print("|", end="")
            for j, cols in enumerate(rows):
                if self.bomb_res[i][j]>0:
                    print(Back.LIGHTRED_EX+" ", end = "")
                elif self.boss_res[i][j]>0:
                    print(Back.MAGENTA + " ", end="")
                elif self.bullet_res[i][j]>0:
                    print(Fore.RED + "|", end = "")
                elif self.power_res[i][j]>0:
                    pu_type = 0
                    for pu in config.fall_powerup:
                        if pu.id == self.power_res[i][j]:
                            pu_type = pu.power
                            break
                    if pu_type == 1:
                        print(Fore.CYAN+"L", end ="")
                    elif pu_type == 2:
                        print(Fore.CYAN + "S", end = "")
                    elif pu_type == 3:
                        print(Fore.CYAN + "T", end = "")
                    elif pu_type == 4:
                        print(Fore.CYAN + "F", end = "")
                    elif pu_type == 5:
                        print(Fore.CYAN + "P", end = "")
                    elif pu_type == 6:
                        print(Fore.CYAN + "X", end = "")
                else:
                    if self.res[i][j] == 0:
                        print(Back.WHITE + " ", end = "")
                    elif self.res[i][j] == -1:
                        print("\n", end = "")
                    elif self.res[i][j] == -2:
                        if ((j == 0 or self.res[i][j-1]!=-2) or (j==self.x_pix-1 or self.res[i][j+1]!=-2)) and config.paddle_shooter == True:
                            print(Back.RED + " ", end ="")
                        else:
                            print(Back.BLUE + " ", end = "")
                    elif self.res[i][j] == -3:
                        print(Back.BLACK + " ", end = "")
                    elif self.res[i][j]>0:
                        strength = 0
                        for o in config.bricks:
                            if int(o.id) == self.res[i][j]:
                                strength = o.strength
                                break
                        if strength == 3:
                            print(Back.RED + " ", end = "")
                        elif strength == 2:
                            print(Back.YELLOW + " ", end = "")
                        elif strength == 1:
                            print(Back.GREEN + " ", end = "") 
                        elif strength == 0:
                            print(Back.WHITE + " ", end = "")  
                        elif strength == 4:
                            print(Back.LIGHTBLACK_EX + " ", end = "")
                        elif strength == 5:
                            print(Back.MAGENTA + " ", end = "")
        print(Back.RESET+Fore.RESET+"Lives: " + str(config.lives))
        print(Back.RESET+Fore.RESET+"Time: " + str(int((int(time()-config.start_time))/60))+ (":" if (len(str((int(time()-config.start_time))%60))==2) else ":0")+ str((int(time()-config.start_time))%60))
        if config.bullet_time>0:
            print(Back.RESET+Fore.RESET+"Score: " + str(config.score)+ "\t\tBullet time: " +("0" if (config.bullet_time<10) else "")+ str(int(config.bullet_time)))
        else:
            print(Back.RESET+Fore.RESET+"Score: " + str(config.score)+"                                            ")
        if config.level==2:
            print("Boss Health: ", end = "")
            for ggg in range(10):
                if ggg<config.boss_health:
                    print("#", end = "")
                else:
                    print("-", end = "")

        # print(config.second_way)
        # print(config.no_bricks)
                # print(cols, end="")
        # for i in range(self.x_pix+1):
        #     print(Back.RESET + "‾", end="")
        for i in range(self.y_pix+4):
            print("\033[F", end = "")
            # if config.level==2:
            #     print("\033[F", end = "")
