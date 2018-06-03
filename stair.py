from pico2d import *
from player import Player

class Stair:

    realx, realy = 100, 70
    def __init__(self):
        self.x, self.y = 100, 70
        self.flag = 0
        self.top, self.bottom = 0, 0
        self.left, self.right = 0, 0

    def get_xy(self):
        return self.x, self.y



    def get_bb(self):
        self.top = self.y + 14
        self.bottom = self.y - 16
        self.left = self.x - 17 - Player.camerax
        self.right = self.x + 15 - Player.camerax
        return self.x - 17 - Player.camerax, self.y - 16, self.x + 15 - Player.camerax, self.y + 14

