from pico2d import *
from player import Player

class Pipe:

    realx, realy = 100, 70

    def __init__(self):
        self.x, self.y = 100, 70
        self.flag = 0
        self.top, self.bottom = 0, 0
        self.left, self.right = 0, 0

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        self.left = self.x - 25 - Player.camerax
        self.right = self.x + 25 - Player.camerax
        if self.flag == 1:
            self.top = self.y + 40
            self.bottom = self.y - 40
            return self.x - 25 - Player.camerax, self.y - 40, self.x + 25 - Player.camerax, self.y + 40
        elif self.flag == 2:
            self.top = self.y + 70
            self.bottom = self.y - 40
            return self.x - 25 - Player.camerax, self.y - 40, self.x + 25 - Player.camerax, self.y + 70
        elif self.flag == 3:
            self.top = self.y + 13
            self.bottom = self.y - 40
            return self.x - 25 - Player.camerax, self.y - 40, self.x + 25 - Player.camerax, self.y + 13

    def get_xy(self):
        return self.x, self.y
