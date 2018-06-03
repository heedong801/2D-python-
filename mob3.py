from pico2d import *
from player import Player

class Monster3:
    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPEED_KMPH = 5.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    distance = 0
    realx, realy = 100, 70

    def __init__(self):
        self.x, self.y = 1795, 450
        self.image = load_image('mob3.png')
        self.top, self.bottom = 0, 0
        self.left, self.right = 0 , 0
        self.flag = False
    def get_xy(self):
        return self.x, self.y

    def draw(self, frame_time):
        self.image.clip_draw(0, 0, 32, 46, self.x - Player.camerax, self.y)


    def update(self, frame_time):
        if Player.realx > 1710 or self.flag == True:
            Monster3.distance = Monster3.RUN_SPEED_PPS * frame_time
            self.y -=  13 * Monster3.distance
            self.flag = True

    def get_bb(self):
        self.top = self.y + 23
        self.bottom = self.y - 23
        self.left = self.x - 15
        self.right = self.x + 15
        return self.x - 15 - Player.camerax, self.y - 23, self.x + 15 - Player.camerax, self.y + 23
