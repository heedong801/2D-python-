from pico2d import *
from player import Player

class Monster1:
    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPEED_KMPH = 5.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    distance = 0

    realx, realy = 100, 70

    def __init__(self):
        self.x, self.y = 100, 70
        self.movestatus = False
        self.image = load_image('mob1.png')
        self.top, self.bottom = 0, 0
        self.left, self.right = 0 , 0
        self.dir = -1
    def get_xy(self):
        return self.x, self.y

    def draw(self, frame_time):
        if self.dir == -1:
            self.image.clip_draw(0, 29, 32, 29, self.x, self.y)
        else:
            self.image.clip_draw(0, 0, 32, 29, self.x, self.y)
    def update(self, frame_time):
        if (self.x - Player.realx < 400 or self.x - Player.realx < -300):
            if self.movestatus == False:
                Monster1.distance = Monster1.RUN_SPEED_PPS * frame_time
                if Player.mob1speedup == False:
                    self.x += self.dir * Monster1.distance
                else:
                    if self.dir == -1:
                        if Player.Right_push == True:
                            self.x += self.dir * 5 * Monster1.distance
                        else:
                            self.x += self.dir * Monster1.distance
                    else:
                        if Player.Right_push == True:
                            self.x -= self.dir * 2 * Monster1.distance
                        else:
                            self.x += self.dir * 1* Monster1.distance

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        self.top = self.y + 15
        self.bottom = self.y - 16
        self.left = self.x - 15
        self.right = self.x + 15
        return self.x - 15, self.y - 16, self.x + 15, self.y + 13
