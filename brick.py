import numpy as np
import config 
from random import randint
from powerup import PowerUp

class Brick:
    def __init__(self, x, y, id, strength):
        self.pos = [y, x]
        self.width = config.brick_len
        self.height = 1
        self.id = id
        self.strength = strength

    
    def createBrick(self, Board):
        for br in config.bricks:
            if br.id == 0:
                config.bricks.remove(br)
        for i in range(self.pos[0], self.pos[0]+self.height):
            for j in range(self.pos[1], self.pos[1]+self.width):
                Board.res[i][j] = self.id
    
    def hit_brick(self, Board):
        if self.strength==1 or self.strength==2 or self.strength==3:
            self.strength = self.strength - 1
        if self.strength==0: 
            if randint(1,5) == 1:
                config.fall_powerup.append(PowerUp(self, Board, len(config.fall_powerup)+1, np.random.choice([1,2,3,4,5])))
            config.score=config.score+10
            config.no_bricks = config.no_bricks - 1
            self.id = 0
            self.createBrick(Board)
    
    def destroy_brick(self, Board):
        if self.strength<=1:
            config.score=config.score+10
            config.no_bricks = config.no_bricks - 1
        self.hit_brick(Board)
        # if self.strength!= 4:
        self.strength = 0
        self.id = 0
        self.createBrick(Board)

class ExplosiveBrick(Brick):
    def __init__(self,x,y,id,strength=5):
        Brick.__init__(self,x,y,id,strength)

    def hit_brick(self,Board):
        self.strength = 0
        self.id = 0
        config.score=config.score+10
        config.no_bricks = config.no_bricks - 1
        self.createBrick(Board)
        if Board.res[self.pos[0] - 1][self.pos[1]]>0:
            for brick in config.bricks:
                if Board.res[self.pos[0] -1][self.pos[1]] == brick.id :
                    brick.destroy_brick(Board)
        if Board.res[self.pos[0] - 1][self.pos[1]-1]>0:
            for brick in config.bricks:
                if Board.res[self.pos[0] -1][self.pos[1]-1] == brick.id :
                    brick.destroy_brick(Board)
        if Board.res[self.pos[0]][self.pos[1]-1]>0:
            for brick in config.bricks:
                if Board.res[self.pos[0]][self.pos[1]-1] == brick.id :
                    brick.destroy_brick(Board)
        if Board.res[self.pos[0] + self.height][self.pos[1]]>0:
            for brick in config.bricks:
                if Board.res[self.pos[0] + self.height][self.pos[1]] == brick.id :
                    brick.destroy_brick(Board)
        if Board.res[self.pos[0] + self.height][self.pos[1] + self.width]>0:
            for brick in config.bricks:
                if Board.res[self.pos[0] +self.height][self.pos[1]+self.width] == brick.id :
                    brick.destroy_brick(Board)
        if Board.res[self.pos[0]][self.pos[1] + self.width]>0:
            for brick in config.bricks:
                if Board.res[self.pos[0]][self.pos[1]+ self.width] == brick.id :
                    brick.destroy_brick(Board)
        if Board.res[self.pos[0] + self.height][self.pos[1] -1]>0:
            for brick in config.bricks:
                if Board.res[self.pos[0] +self.height][self.pos[1]-1] == brick.id :
                    brick.destroy_brick(Board)
        if Board.res[self.pos[0] - 1][self.pos[1] + self.width]>0:
            for brick in config.bricks:
                if Board.res[self.pos[0] -1][self.pos[1]+ self.width] == brick.id :
                    brick.destroy_brick(Board)