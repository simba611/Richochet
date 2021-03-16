import numpy as np

class Paddle:
    def __init__(self, length, Board):
        self.length = length
        self.pos=int(Board.x_pix/2 - length/2)

    def draw_paddle(self, Board):
        for i in range(Board.x_pix):
            Board.res[Board.y_pix-1][i] = 0
        for i in range(self.length):
            Board.res[Board.y_pix-1][self.pos+i] = -2

    def mov_paddle(self, dir, Board, Ball):
        if dir == "a":
            if self.pos != 0:
                if (Ball.paddle_attach == True and Board.res[Ball.pos[0]+1][Ball.pos[1]] == -2):
                    Ball.next_pos[1] = Ball.next_pos[1] - 1
                    Ball.pos[1] = Ball.pos[1] - 1
                    Ball.draw_ball(Board)
                    Ball.ini_pos[0] = Board.y_pix-2
                    Ball.ini_pos[1] = Ball.pos[1]
                self.pos = self.pos-1
        elif dir == "d":
            if self.pos + self.length != Board.x_pix:
                if (Ball.paddle_attach == True and Board.res[Ball.pos[0]+1][Ball.pos[1]] == -2):
                    Ball.next_pos[1] = Ball.next_pos[1] + 1
                    Ball.pos[1] = Ball.pos[1] + 1
                    Ball.draw_ball(Board)
                    Ball.ini_pos[0] = Board.y_pix-2
                    Ball.ini_pos[1] = Ball.pos[1]
                self.pos = self.pos + 1
        else:
            # print("yes", end="")
            if (Ball.paddle_attach == True and Board.res[Ball.pos[0]+1][Ball.pos[1]] == -2):
                Ball.draw_ball(Board)
                Ball.ini_pos[0] = Board.y_pix-2
                Ball.ini_pos[1] = Ball.pos[1] 
        # Ball.dist_paddle = Ball.pos[1] - self.pos
        self.draw_paddle(Board)
