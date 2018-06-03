import game_framework
import title_state
import json
import math
import random
import end

from pico2d import *
from player import Player
from background import Background
from mob1 import Monster1
from pipe import Pipe
from stair import Stair
from block import Block
from traproad import Traproad
from mushroom import Mushroom
from muscle import Muscleman
from cloud import Cloud
from mob2 import Monster2
from mob3 import Monster3

name = "MainState"

player = None
cloud = None
background = None
blocks = None
pipes = None
mob1s = None
stairs = None
traproad = None
mush = None
muscle = None
mob2 = None
mob3 = None
result = True
resultBlock = -1
resultBack = False

index = 0

def create_mobs():
    team_data_text1 = '\
                {\
                    "1" : {"x" : 300, "y" : 70, "dir" : -1 },\
                    "2" : {"x" : 500, "y" : 70, "dir" : -1 },\
                    "3" : {"x" : 700, "y" : 70, "dir" : -1}\
                }\
                '
    team_data = json.loads(team_data_text1)

    team = []
    for num in team_data:
        player = Monster1()
        player.x = team_data[num]['x']
        player.y = team_data[num]['y']
        player.dir = team_data[num]['dir']
        player.realx = player.x
        player.realy = player.y
        team.append(player)
    return team

def create_stairs():
    team_data_text4 = '\
                {\
                    "1": {"x": 2606, "y": 70}, \
                    "2": {"x": 2638, "y": 100}, \
                    "3": {"x": 2670, "y": 130}, \
                    "4": {"x": 2800, "y": 130}, \
                    "5": {"x": 2832, "y": 100}, \
                    "6" : {"x" : 3440, "y" : 70 },\
                    "7" : {"x" : 3472, "y" : 100},\
                    "8" : {"x" : 3504, "y" : 130},\
                    "9" : {"x" : 3536, "y" : 158},\
                    "10" : {"x" : 3568, "y" : 187 },\
                    "11" : {"x" : 3600, "y" : 216},\
                    "12" : {"x" : 3632, "y" : 245},\
                    "13" : {"x" : 3664, "y" : 274},\
                    "14" : {"x" : 3696, "y" : 274}\
                }\
                '
    team_data = json.loads(team_data_text4)

    team = []
    for num in team_data:
        player = Stair()
        player.x = team_data[num]['x'] + 34
        player.y = team_data[num]['y']
        player.realx = player.x
        player.realy = player.y
        team.append(player)
    return team

def create_pipes():
    team_data_text3 = '\
                {\
                    "1" : {"x" : 642, "y" : 100, "flag": 1 },\
                    "2" : {"x" : 935, "y" : 100, "flag" : 2 },\
                    "3" : {"x" : 3035, "y" : 100, "flag" : 1},\
                    "4" : {"x" : 3389, "y" : 100, "flag" : 3}\
                }\
                '
    team_data = json.loads(team_data_text3)

    team = []
    for num in team_data:
        player = Pipe()
        player.x = team_data[num]['x'] + 34
        player.y = team_data[num]['y']
        player.flag = team_data[num]['flag']
        player.realx = player.x
        player.realy = player.y
        team.append(player)
    return team


def create_blocks():
    team_data_text2 = '\
                {\
                    "1" : {"x" : 273, "y" : 160, "shape" : 2, "alpha" : 0},\
                    "2" : {"x" : 369, "y" : 160, "shape" : 1, "alpha" : 0},\
                    "3" : {"x" : 401, "y" : 160, "shape" : 2, "alpha" : 0},\
                    "4" : {"x" : 433, "y" : 160, "shape" : 1, "alpha" : 0},\
                    "5" : {"x" : 465, "y" : 160, "shape" : 2, "alpha" : 0},\
                    "6" : {"x" : 497, "y" : 160, "shape" : 1, "alpha" : 0},\
                    "7" : {"x" : 433, "y" : 280, "shape" : 1, "alpha" : 0},\
                    "8" : {"x" : 1484, "y" : 160, "shape" : 1, "alpha" : 0},\
                    "9" : {"x" : 1517, "y" : 160, "shape" : 2, "alpha" : 0},\
                    "10" : {"x" : 1549, "y" : 160, "shape" : 1, "alpha" : 0},\
                    "11" : {"x" : 1582, "y" : 280, "shape" : 1, "alpha" : 0},\
                    "12" : {"x" : 1615, "y" : 280, "shape" : 1, "alpha" : 0},\
                    "13" : {"x" : 1648, "y" : 280, "shape" : 3, "alpha" : 2},\
                    "14" : {"x" : 1680, "y" : 280, "shape" : 1, "alpha" : 2},\
                    "15" : {"x" : 1712, "y" : 280, "shape" : 1, "alpha" : 2},\
                    "16" : {"x" : 1841, "y" : 280, "shape" : 1, "alpha" : 0},\
                    "17" : {"x" : 1873, "y" : 280, "shape" : 1, "alpha" : 0},\
                    "18" : {"x" : 1905, "y" : 280, "shape" : 1, "alpha" : 0},\
                    "19" : {"x" : 1905, "y" : 160, "shape" : 1, "alpha" : 0},\
                    "20" : {"x" : 2128, "y" : 160, "shape" : 1, "alpha" : 0},\
                    "21" : {"x" : 2160, "y" : 160, "shape" : 1, "alpha" : 0},\
                    "22" : {"x" : 2290, "y" : 160, "shape" : 2, "alpha" : 0},\
                    "23" : {"x" : 2386, "y" : 160, "shape" : 2, "alpha" : 0},\
                    "24" : {"x" : 2482, "y" : 160, "shape" : 2, "alpha" : 0},\
                    "25" : {"x" : 2386, "y" : 280, "shape" : 2, "alpha" : 0},\
                    "26" : {"x" : 3188, "y" : 160, "shape" : 1, "alpha" : 0},\
                    "27" : {"x" : 3220, "y" : 160, "shape" : 2, "alpha" : 0},\
                    "28" : {"x" : 3252, "y" : 160, "shape" : 1, "alpha" : 0},\
                    "29" : {"x" : 3284, "y" : 160, "shape" : 1, "alpha" : 0},\
                    "30" : {"x" : 1300, "y" : 160, "shape" : 3, "alpha" : 1},\
                    "31" : {"x" : 2865, "y" : 250, "shape" : 3, "alpha" : 1},\
                    "32" : {"x" : 2899, "y" : 130, "shape" : 3, "alpha" : 1},\
                    "33" : {"x" : 2934, "y" : 130, "shape" : 3, "alpha" : 1},\
                    "34" : {"x" : 2969, "y" : 130, "shape" : 3, "alpha" : 1},\
                    "35" : {"x" : 3004, "y" : 130, "shape" : 3, "alpha" : 1}\
                  }\
                  '

    team_data = json.loads(team_data_text2)

    team = []
    for num in team_data:
         player = Block()
         player.x = team_data[num]['x']
         player.y = team_data[num]['y']
         player.flag = team_data[num]['shape']
         player.alpha = team_data[num]['alpha']
         team.append(player)
    return team

def enter():
    global background, player, mob1s, blocks, pipes, stairs, traproad, mush, muscle,cloud, mob2, mob3
    background = Background()
    player = Player()
    mob1s = create_mobs()
    blocks = create_blocks()
    pipes = create_pipes()
    stairs = create_stairs()
    traproad = Traproad()
    mush = Mushroom()
    muscle = Muscleman()
    cloud = Cloud()
    mob2 = Monster2()
    mob3 = Monster3()
    player.set_background(background)
def exit():
    global background, player, mob1s, blocks,pipes,stairs, traproad, mush, muscle,cloud, mob2, mob3
    del(background)
    del(player)
    del(traproad)
    del(mush)
    del(muscle)
    del(cloud)
    del(mob2)
    del(mob3)
    for mob in mob1s:
        del(mob)
    del(blocks)
    for pipe in pipes:
        del(pipe)
    for stair in stairs:
        del (stair)

def collide(a, b):
    global index
    left_a, bottom_a, right_a, top_a = a.get_bb()
    if a == player and b == background:
        left_b, bottom_b, right_b, top_b = b.get_bb(Player)
    elif a == mob1s[index] and b == background :
        left_b, bottom_b, right_b, top_b = b.get_bb(mob1s[index])
    else:
        left_b, bottom_b, right_b, top_b = b.get_bb()
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a - 7< bottom_b: return False
    if bottom_a > top_b: return False

    return True

def collideKind(a, b):
    midx_a, midy_a = a.get_xy()
    midx_b, midy_b = b.get_xy()

    result = (midy_b - midy_a) / (midx_b - midx_a)

    return result

def pause():
    pass

def resume():
    pass

def handle_events(frame_time):
    global die
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_F1:
            die = True
            Player.death_sound.play()
        elif Player.realx > 4378:
            game_framework.change_state(end)
        elif Player.die == True:
            Player.die = False
            Player.Left_push = False
            Player.Right_push = False
            Player.distance = 0
            Player.camerax = 40
            Player.realx = 40
            Player.realy = 0
            Player.mob1speedup = False
            Player.moveableL = True
            Player.moveableR = True
            Player.jumpable = True
            Player.muscleman = False
            Player.status = 0
            player.y = 75
            player.x = 40
            player.Jump_state = False
            player.direction = Player.RIGHT_STAND
            game_framework.change_state(title_state)
            enter()
        else:
            player.handle_event(event)

current_time = 0.0

def get_frame_time():
    global current_time

    frame_time = get_time() - current_time
    current_time += frame_time
    return frame_time

def draw_scene(frame_time):
    background.draw(Player, frame_time)
    player.draw(frame_time)
    traproad.draw(frame_time)
    cloud.draw(frame_time)
    if Player.muscleman == True:
        muscle.draw(frame_time)
    if Mushroom.flag == True:
        mush.draw(frame_time)
    for mob in mob1s:
        mob.draw(frame_time)
    for block in blocks:
        if not block.alpha == 1:
            block.draw(frame_time)
    mob2.draw(frame_time)
    mob3.draw(frame_time)

def update(frame_time):
    global index
    index = 0
    pipeCollideidx = -2
    blockCollideidx = -2
    stairCollideidx = -2
    fall = False
    Player.jumpable = True
    player.update(frame_time)
    traproad.update(frame_time)
    muscle.update(frame_time)
    mob2.update(frame_time)
    mob3.update(frame_time)
    for i in range( 0, len(blocks)):
        if blocks[i].alpha == 2:
            blocks[i].update(frame_time)
    if Player.muscleman == True:
        player.y += (-2) * Player.distance

    if not player.die:
        if not collide(player, background):
            for i in range(0,len(pipes)):
                if not collide(player, pipes[i]):
                    fall = True
                else:
                    if (player.right - 2 < pipes[i].right and player.right - 2 > pipes[i].left) or (
                                player.left + 2 > pipes[i].left and player.left + 2 < pipes[i].right):
                        fall = False
                        pipeCollideidx = i
                        break
            if fall:
                for i in range(0,len(blocks)):
                    if not collide(player, blocks[i]):
                        fall = True
                    else:
                        result = collideKind(player, blocks[i])
                        if blocks[i].alpha == 1:
                            if Player.status in (Player.RIGHT_JUMPUP, Player.LEFT_JUMPUP) and player.top > blocks[i].bottom and player.top < blocks[i].top:
                                blocks[i].alpha = 0
                                fall = True
                                player.y += (-1) * player.distance
                                break
                        elif blocks[i].alpha == 2 and player.y < 160:
                            Player.die = True
                            Player.death_sound.play()
                        elif (player.right - 2 < blocks[i].right and player.right -2 > blocks[i].left) or (
                                    player.left + 2 > blocks[i].left and player.left + 2 < blocks[i].right):
                            fall = False

                            if blocks[i].flag == 2 and  player.top < blocks[i].top:
                                blocks[i].flag = 3
                                if blocks[i].x == 401:
                                    Mushroom.flag = True
                                    mush.x = blocks[i].x
                                    mush.y = blocks[i].y + 32
                            blockCollideidx = i
                            break

                if fall:
                    for i in range(0, len(stairs)):
                        if not collide(player, stairs[i]):
                            fall = True
                        else:
                            if (player.right -2< stairs[i].right and player.right-2> stairs[i].left) or (
                                        player.left+ 2 > stairs[i].left and player.left +2< stairs[i].right):
                                fall = False
                                stairCollideidx = i
                                break

                    if fall:
                        if player.Jump_state == 0:
                            player.y += (-1) * player.distance
                            Player.jumpable = False
                        else:
                            if player.direction in (player.RIGHT_JUMPDOWN, player.LEFT_JUMPDOWN):
                                player.y += (-1.5) * player.distance
                                player.y = round(player.y)
                                Player.jumpable = False

        elif collide(player, background):
            if player.Jump_state == 1 and player.direction in ( player.LEFT_JUMPDOWN, player.RIGHT_JUMPDOWN):
                player.Jump_state = 0

            for i in range(0, len(blocks)):
                if collide(player, blocks[i]):
                    if blocks[i].alpha == 2 and player.y < 160:
                        Player.die = True
                        Player.death_sound.play()

        if pipeCollideidx >= 0:
            result = collideKind(player, pipes[pipeCollideidx])
            if abs(result) > 2:
                Player.moveable = True
                if player.Jump_state == 1 and player.direction in ( player.LEFT_JUMPDOWN, player.RIGHT_JUMPDOWN):
                    player.Jump_state = 0
                elif player.Jump_state == 1 and player.direction in ( player.LEFT_JUMPUP, player.RIGHT_JUMPUP):
                    if player.direction == player.LEFT_JUMPUP:
                        player.direction = player.LEFT_JUMPDOWN
                    elif player.direction == player.RIGHT_JUMPUP:
                        player.direction = player.RIGHT_JUMPDOWN

                    player.y += (-1) * player.distance

        if stairCollideidx >= 0:
            result = collideKind(player, stairs[stairCollideidx])
            if abs(result) > 1:
                if player.Jump_state == 1 and player.direction in ( player.LEFT_JUMPDOWN, player.RIGHT_JUMPDOWN):
                    player.Jump_state = 0
                elif player.Jump_state == 1 and player.direction in ( player.LEFT_JUMPUP, player.RIGHT_JUMPUP):
                    if player.direction == player.LEFT_JUMPUP:
                        player.direction = player.LEFT_JUMPDOWN
                    elif player.direction == player.RIGHT_JUMPUP:
                        player.direction = player.RIGHT_JUMPDOWN

                    player.y += (-2) * player.distance

        if blockCollideidx >= 0:
            result = collideKind(player, blocks[blockCollideidx])
            if abs(result) > 1:
                if player.Jump_state == 1 and player.direction in ( player.LEFT_JUMPDOWN, player.RIGHT_JUMPDOWN):
                    player.Jump_state = 0
                elif player.Jump_state == 1 and player.direction in ( player.LEFT_JUMPUP, player.RIGHT_JUMPUP):
                    if player.direction == player.LEFT_JUMPUP:
                        player.direction = player.LEFT_JUMPDOWN
                    elif player.direction == player.RIGHT_JUMPUP:
                        player.direction = player.RIGHT_JUMPDOWN

                    player.y += (-2) * player.distance
        if collide(player, mush):
            Player.powerup_sound.play()
            Mushroom.flag = False
            Player.muscleman = True
            mush.y = 20000


        moveableL1 = True
        moveableR1 = True
        moveableR2 = True
        moveableL2 = True
        moveableR3 = True
        moveableL3 = True
        moveableR4 = True
        moveableL4 = True

        if collide(player, background):
            if player.bottom < background.top:
                if player.left < background.left:
                    moveableR1 = False
                    moveableL1 = True
                elif player.right > background.right:
                    moveableR1 = True
                    moveableL1 = False
                else:
                    moveableR1 = True
                    moveableL1 = True
            else:
                if player.left < background.left:
                    moveableR1 = False
                    moveableL1 = True
                elif player.right > background.right:
                    moveableR1 = True
                    moveableL1 = False
                else:
                    moveableR1 = True
                    moveableL1 = True

        for i in range(0, len(pipes)):
            if collide(player, pipes[i]):
                if player.bottom < pipes[i].top:
                    if player.left < pipes[i].left:
                        moveableR1 = False
                        moveableL1 = True
                    elif player.right > pipes[i].right:
                        moveableR1 = True
                        moveableL1 = False
                    break
                else:
                    moveableR1 = True
                    moveableL1 = True
            else:
                moveableR1 = True
                moveableL1 = True

        for i in range(0, len(stairs)):
            if collide(player, stairs[i]):
                if player.bottom < stairs[i].top:
                    if player.left < stairs[i].left:
                        moveableR2 = False
                        moveableL2 = True
                    elif player.right > stairs[i].right:
                        moveableR2 = True
                        moveableL2 = False
                    break
                else:
                    moveableR2 = True
                    moveableL2 = True
            else:
                moveableR2 = True
                moveableL2 = True

        for i in range(0, len(blocks)):
            if blocks[i].alpha != 1:
                if collide(player, blocks[i]):
                    if player.bottom < blocks[i].top:
                        if player.left < blocks[i].left:
                            moveableR3 = False
                            moveableL3 = True
                        elif player.right > blocks[i].right:
                            moveableR3 = True
                            moveableL3 = False
                        break
                    else:
                        moveableR3 = True
                        moveableL3 = True
                else:
                    moveableR3 = True
                    moveableL3 = True

        if not moveableL1 or not moveableL2 or not moveableL3:
            Player.moveableL = False
        else:
            Player.moveableL = True
        if not moveableR1 or not moveableR2 or not moveableR3:
            Player.moveableR = False
        else:
            Player.moveableR = True


    for mob in mob1s:
        if collide(player, mob):
            if Player.die == False:
                Player.die = True
                Player.death_sound.play()

    if collide(player, cloud):
        if Player.die == False:
            Player.die = True
            cloud.alpha = 0
            Player.death_sound.play()

    if collide(player, mob2):
        if Player.die == False:
            Player.die = True
            Player.death_sound.play()

    if collide(player, mob3):
        if Player.die == False:
            Player.die = True
            Player.death_sound.play()

    for i in range(0,len(mob1s)):
        mobfall = False
        mob1s[i].movestatus = False
        index = i
        if not collide(mob1s[i], background):
            for j in range(0,len(pipes)):
                if not collide(mob1s[i], pipes[j]):
                    mobfall = True
                else:
                    mobfall = False
                    break
            if mobfall:
                for j in range(0,len(blocks)):
                    if not collide(mob1s[i], blocks[j]):
                        mobfall = True
                    else:
                        mobfall = False
                        break

                if mobfall:
                    for j in range(0, len(stairs)):
                        if not collide(mob1s[i], stairs[j]):
                            mobfall = True
                        else:
                            mobfall = False
                            break

                    if mobfall:
                        mob1s[i].movestatus = True
                        if i != 4 and i != 7:
                            mob1s[i].y += (-2) * Monster1.distance
        else:
            for j in range(0, len(pipes)):
                if collide(mob1s[i], pipes[j]):
                    mob1s[i].dir *= -1
                    mob1s[i].x += mob1s[i].dir * Monster1.distance

    for mob in mob1s:
        mob.update(frame_time)


def draw(frame_time):
    clear_canvas()
    draw_scene(frame_time)
    update_canvas()




