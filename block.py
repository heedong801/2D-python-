from pico2d import *
from player import Player

class Block:
    fall = False
    def __init__(self):
        self.x, self.y = 200, 160
        self.top, self.bottom = 0, 0
        self.left, self.right = 0, 0
        self.flag = 1
        self.alpha = 0
        self.image = load_image('Block.png')

    def GetAlpha(self):
        return self.alpha

    def draw(self, frame_time):

        self.image.clip_draw(self.flag * 33, 67, 32, 33, self.x - Player.camerax, self.y)
    def update(self, frame_time):
        if Player.realx > 1600 and self.alpha == 2 or Block.fall == True:
            if Player.realy < 200:
                self.y -= 4
                Block.fall = True

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        self.top = self.y + 16
        self.bottom = self.y - 16
        self.left = self.x - Player.camerax - 17
        self.right = self.x - Player.camerax + 15
        return self.x - Player.camerax - 17, self.y - 16, self.x - Player.camerax + 15, self.y + 16

    def get_xy(self):
        return self.x, self.y
