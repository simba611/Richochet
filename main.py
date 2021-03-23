from os import system
from random import randint
from time import process_time, sleep, time

from colorama import Back, Fore, Style

import config
from ball import Ball
from board import Board
from brick import Brick, ExplosiveBrick, RainbowBrick
from input import *
from paddle import Paddle
from bullet import Bullet
from boss import Boss
from bomb import Bomb

x_pixel = 100
y_pixel = 40
paddle_len = 20
power_time = 15

def use_input(arg):
    if arg == "q":
        system("stty echo")
        exit()
    else:
        paddle.mov_paddle(arg, box, ball, boss)
        paddle.mov_paddle(arg, box, ball, boss)

system("stty -echo")


def createLayout():
    count = 1
    for i in range(y_pixel-int(y_pixel/2)):
        if i>y_pixel/10:
            for j in range(((int(int(x_pixel/2)/config.brick_len)))):
                if j != 0:
                    if(randint(0,4)==1):
                        rand = randint(1,4)
                        if rand == 4:
                            if randint(0,1) == 1:
                                rand = randint(1,3)
                        if rand !=4:
                            config.no_bricks = config.no_bricks+2
                        if(randint(1,10)==1):
                            config.bricks.append(RainbowBrick(config.brick_len*j,i,count, rand))
                            config.bricks.append(RainbowBrick(x_pixel - config.brick_len -config.brick_len*j,i,count+1, rand))
                        else:
                            config.bricks.append(Brick(config.brick_len*j,i,count, rand))
                            config.bricks.append(Brick(x_pixel - config.brick_len -config.brick_len*j,i,count+1, rand))
                        count = count + 2
    # for b in config.bricks:
    #     print(str(b.pos[0])+ " " + str(b.pos[1]))
    for i in range(y_pixel - int(y_pixel/2)):
        save = i
        if i > y_pixel/10:
            if randint(1,7) == 5:
                for j in range(1, ((int(int(x_pixel/2)/config.brick_len)))):
                    if ((int(int(x_pixel/2)/config.brick_len))) - j*config.brick_len > 2:
                        rand_len = randint(7, 11)
                        while j < ((int(int(x_pixel/2)/config.brick_len))) and j < rand_len:
                            for br in config.bricks:
                                if br.pos[0] == save and (br.pos[1] == config.brick_len*j):
                                    # print("hello " + str(br.pos[0]) + " " + str(br.pos[1])) 
                                    if br.strength != 4:
                                        config.no_bricks = config.no_bricks - 1
                                    config.overlap = config.overlap + 2
                                    config.bricks.remove(br)
                            config.bricks.append(ExplosiveBrick(config.brick_len*j,save,count))
                            config.no_bricks = config.no_bricks + 1
                            for br in config.bricks:
                                if br.pos[0] == save and br.pos[1] == (x_pixel - config.brick_len- config.brick_len*j):
                                    # print("hell "+str(br.pos[0]) + " " + str(br.pos[1])) 
                                    if br.strength != 4:
                                        config.no_bricks = config.no_bricks - 1
                                    config.bricks.remove(br)
                            config.bricks.append(ExplosiveBrick(x_pixel - config.brick_len-config.brick_len*j,save,count+1))
                            config.no_bricks = config.no_bricks + 1
                            count = count + 2
                            up = randint(1,3)
                            if up == 1:
                                save = save+1
                            j = j+1
                        break


def createLayoutBoss():
    count = 1
    for i in range(y_pixel-int(y_pixel/2)):
        if i>y_pixel/10:
            for j in range(((int(int(x_pixel/2)/config.brick_len)))):
                if j != 0:
                    if(randint(0,4)==1):
                        rand = randint(1,4)
                        if rand == 4:
                            if randint(0,1) == 1:
                                rand = randint(1,3)
                        if rand !=4:
                            config.no_bricks = config.no_bricks+2
                        if(randint(0,5)==1):
                            config.bricks.append(Brick(config.brick_len*j,i,count, 4))
                            config.bricks.append(Brick(x_pixel - config.brick_len -config.brick_len*j,i,count+1, 4))
                        count = count + 2
        # elif i == (y_pixel/10)-2:
        #     for j in range(((int(int(x_pixel/2)/config.brick_len)))):
        #         if j != 0:
        #             # if(randint(0,4)==1):
        #             #     rand = randint(1,4)
        #             #     if rand == 4:
        #             #         if randint(0,1) == 1:
        #             #             rand = randint(1,3)
        #             #     if rand !=4:
        #             #         config.no_bricks = config.no_bricks+2
        #             config.bricks.append(Brick(config.brick_len*j,i,count, 3))
        #             config.bricks.append(Brick(x_pixel - config.brick_len -config.brick_len*j,i,count+1, 3))
        #             count = count + 2


next_level_flag = 0
for levell in range(3):
    boss = Boss(int(x_pixel/2 - config.boss_length/2))
    config.level = levell
    config.bricks.clear()
    if levell==2:
        createLayoutBoss()
    else:
        createLayout()

    config.start_time = time()
    while True:
        if config.lives <= 0:
            for hh in range(box.y_pix + 4):
                for jj in range(box.x_pix):
                    print(" ", end = "")
                print("")
            for hh in range(box.y_pix + 4):
                print("\033[F", end = "")
            print("Game Over")
            print(Back.RESET+Fore.RESET+"Lives: " + str(config.lives))
            # print(Back.RESET+Fore.RESET+"Time: " + str(int((int(time()-config.start_time))/60))+ (":" if (len(str((int(time()-config.start_time))%60))==2) else ":0")+ str((int(time()-config.start_time))%60))
            print(Back.RESET+Fore.RESET+"Score: " + str(config.score))
            system("stty echo")
            quit()
        box = Board(x_pixel, y_pixel)
        paddle = Paddle(paddle_len, box)
        ball = Ball(box, paddle)
        for br in config.bricks:
            br.createBrick(box)
        ball.draw_ball(box)
        config.active_powerup.clear()
        fast_iter = 0
        brick_time = time()
        config.paddle_shooter=False
        config.bullet.clear()
        shoott_it = 0
        kk = 0
        config.bullet_time=0
        config.through_ball = False
        config.life_end=False 
        if next_level_flag==1:
            next_level_flag=0
            break
        while True:
            if(time()- brick_time > config.brick_fall_time):
                config.brick_fall = True
            else:
                config.brick_fall = False
            config.second_way = 0
            for second in config.bricks:
                if second.id != 0 and second.strength != 4:
                    config.second_way = config.second_way + 1
            if levell!=2:
                if config.second_way == 0:
                    next_level_flag=1
                    break
            key = input_to(Get())
            if key != None:
                sleep(0.02)
            if(key=="w"):
                if ball.paddle_attach == True and box.res[ball.pos[0]+1][ball.pos[1]] == -2:
                    ball.vel[0] = -1*ball.vel[0]
                    if(ball.vel[1]!=0):
                        ball.vel[1] = (ball.vel[1]/abs(ball.vel[1]))*abs(int(paddle.pos + paddle.length/2) - ball.pos[1])
                    else:
                        ball.vel[1] = -1*(int(paddle.pos + paddle.length/2) - ball.pos[1])
                    if ball.vel[1]>4:
                        ball.vel[1] = 4
                    if ball.vel[1]< -4:
                        ball.vel[1] = -4
                    ball.next_pos = [ball.pos[0]-ball.vel[0], ball.pos[1]+ball.vel[1]]
                    ball.prev_pos = [ball.pos[0], ball.pos[1]]
                    ball.ini_pos = [ball.pos[0], ball.pos[1]]
                    ball.angle = ball.vel[1]/ball.vel[0]
                    ball.paddle_attach = False
                    config.paddle_attach=False
                    config.brick_fall_paddle_touch = True
            if(key=="p"):
                next_level_flag=1
                break
            if(key == "q"):
                system("stty echo")
                exit()
            curr = config.lives
            use_input(key)
            ball.mov_ball(box, paddle, boss)
            ball.mov_ball(box, paddle, boss)
            for fast in range(fast_iter):
                ball.mov_ball(box, paddle, boss)
            fast_iter = 0
            for pu in config.fall_powerup:
                pu.fall(paddle, box, ball)
            new_it = 0
            while new_it < len(config.active_powerup):
                if time()-config.active_powerup[new_it].start>power_time:
                    if config.active_powerup[new_it].power == 1:
                        paddle.length = paddle.length - 2
                        if paddle.length<paddle_len:
                            paddle.length = paddle_len
                    if config.active_powerup[new_it].power == 2:
                        if paddle.pos + paddle.length == box.x_pix:
                            paddle.pos = paddle.pos - 2
                        paddle.length = paddle.length + 2
                        if paddle.length > paddle_len:
                            paddle.length = paddle_len
                    if config.active_powerup[new_it].power == 3:
                        config.through_ball = False
                    if config.active_powerup[new_it].power == 6:
                        config.paddle_shooter = False
                        config.bullet_time=0
                    config.active_powerup.remove(config.active_powerup[new_it])
                    new_it = new_it - 1
                new_it = new_it + 1
            config.bullet_time=0
            for pu in config.active_powerup:
                if pu.power == 5:
                    config.paddle_attach=True
                    ball.paddle_attach = True
                if pu.power == 1:
                    if config.no_len_plus > 0:
                        if paddle.length < box.x_pix - 3:
                            if paddle.pos + paddle.length == box.x_pix:
                                paddle.pos = paddle.pos - 2
                            paddle.length = paddle.length + 2
                            config.no_len_plus = config.no_len_plus - 1
                if pu.power == 2:
                    if config.no_len_minus>0:
                        if paddle.length > 8:
                            paddle.length = paddle.length - 2
                            config.no_len_minus = config.no_len_minus - 1
                if pu.power == 4:
                    fast_iter = fast_iter+1
                if pu.power == 3:
                    config.through_ball = True
                if pu.power == 6:
                    if int(pu.start)+power_time-int(time())>config.bullet_time:
                        config.bullet_time=int(pu.start)+power_time-int(time())
                    config.paddle_shooter = True
            if(shoott_it%10==0):
                if config.paddle_shooter == True:
                    config.bullet.append(Bullet(paddle.pos+1, box, len(config.bullet)+1))
                    config.bullet.append(Bullet(paddle.pos+paddle.length, box, len(config.bullet)+1))
            shoott_it = (shoott_it+1)%10

            kk = kk+1
            if levell == 2:
                if (kk%40 == 0):
                    config.bombs.append((Bomb(int(box.y_pix/10 -3), int(boss.pos + boss.length/2))))

                for i in config.bombs:
                    i.bomb_tick(box)
                bomb_iter = 0
                while bomb_iter < len(config.bombs):
                    if config.bombs[bomb_iter].to_remove == True:
                        config.bombs.remove(config.bombs[bomb_iter])
                        bomb_iter=bomb_iter-1
                    bomb_iter=bomb_iter+1

            for i in config.bullet:
                i.tick(box)

            bullet_iter = 0
            while bullet_iter< len(config.bullet):
                if config.bullet[bullet_iter].to_remove == True:
                    config.bullet.remove(config.bullet[bullet_iter])
                    bullet_iter=bullet_iter-1
                bullet_iter= bullet_iter+1
            for i in config.bricks:
                i.tick()
            if config.life_end==True:
                config.lives= config.lives - 1
                break
            paddle.draw_paddle(box)
            if(levell==2):
                boss.draw_boss(box)
            box.print_board()


for hh in range(box.y_pix + 4):
    for jj in range(box.x_pix):
        print(" ", end = "")
    print("")
for hh in range(box.y_pix + 4):
    print("\033[F", end = "")
print("Game Over")
print(Back.RESET+Fore.RESET+"Lives: " + str(config.lives))
# print(Back.RESET+Fore.RESET+"Time: " + str(int((int(time()-config.start_time))/60))+ (":" if (len(str((int(time()-config.start_time))%60))==2) else ":0")+ str((int(time()-config.start_time))%60))
print(Back.RESET+Fore.RESET+"Score: " + str(config.score))
system("stty echo")
quit()
    # print(ball.vel)

 
