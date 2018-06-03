from pico2d import *
from player import Player

class Muscleman:

    def __init__(self):
        self.x, self.y = 100, 70
        self.frame = 0
        self.image = load_image('muscle.png')
        self.top, self.bottom = 0, 0
        self.left, self.right = 0 , 0

    def get_xy(self):
        return self.x, self.y

    def draw(self, frame_time):
        self.image.clip_draw(self.frame * 64, 0, 64, 111, self.x, self.y)

    def update(self, frame_time):
        if Player.status <= 4:
            self.frame = 0
        else:
            self.frame = 1

        self.x ,self.y = Player.realx - Player.camerax + 45, Player.realy
