from pico2d import *
from player import Player

class Cloud:
    def __init__(self):
        self.x, self.y = 3338, 270
        self.top, self.bottom = 0, 0
        self.left, self.right = 0, 0
        self.alpha = 1
        self.image = load_image('Cloud.png')

    def draw(self, frame_time):
        self.image.clip_draw(0, self.alpha * 40, 70, 40, self.x - Player.camerax, self.y)


    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        self.top = self.y + 19
        self.bottom = self.y - 19
        self.left = self.x - Player.camerax - 35
        self.right = self.x - Player.camerax + 35
        return self.x - Player.camerax - 35, self.y - 19, self.x - Player.camerax + 35, self.y + 19

    def get_xy(self):
        return self.x, self.y
