from pico2d import *
from player import Player

class Traproad:
    def __init__(self):
        self.x, self.y = 2385, 25
        self.top, self.bottom = 0, 0
        self.left, self.right = 0, 0
        self.image = load_image('traproad.png')

    def draw(self, frame_time):
        self.image.clip_draw(0, 0, 160, 64, self.x - Player.camerax, self.y)

    def update(self, frame_time):
        if Player.realx > 2278:
            self.y += (-3) * Player.distance


    def get_bb(self):
        self.top = self.y + 16
        self.bottom = self.y - 16
        self.left = self.x - Player.camerax - 17
        self.right = self.x - Player.camerax + 15
        return self.x - Player.camerax - 75, self.y - 48, self.x - Player.camerax + 75, self.y + 16

    def get_xy(self):
        return self.x, self.y
