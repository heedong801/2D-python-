from pico2d import *

from player import Player

class Background:
    gap = 0
    start = 0
    def __init__(self):
        self.top, self.bottom = 0, 0
        self.left, self.right = 0, 0
        self.image = load_image('1map.png')
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h
        self.bgm = load_music('field.wav')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()

    def draw(self, char, frame_time):
        self.image.draw(2240 - Player.camerax , 210, 4480, 420)


    def get_bb(self, char):
        self.top, self.bottom = 55, 0
        if char.realx < 1250:
            self.left, self.right = 0, 1250 - Player.camerax + 32
            if char == Player:
                Background.start = 1250
                Background.gap = 1342 - 1250
            return 0, 0, 1250 - Player.camerax + 32, 55
        elif char.realx > 1342 and char.realx < 1698:
            self.left, self.right = 1342 - Player.camerax + 32, 1698 - Player.camerax + 32
            if char == Player:
                Background.start = 1699
                Background.gap = 1790 - 1698
            return 1342 - Player.camerax + 32, 0, 1698 - Player.camerax + 32, 55
        elif char.realx > 1790 and char.realx < 2278:
            self.left, self.right = 1790 - Player.camerax + 32, 2278 - Player.camerax + 32
            if char == Player:
                Background.start = 2279
                Background.gap = 2428 - 2278
            return 1790 - Player.camerax + 32, 0, 2278 - Player.camerax + 32, 55
        elif char.realx > 2428 and char.realx < 2695:
            self.left, self.right = 2428 - Player.camerax + 32, 2695 - Player.camerax + 32
            if char == Player:
                Background.start = 2696
                Background.gap = 2780 - 2695
            return 2428 - Player.camerax + 32, 0, 2695 - Player.camerax + 32, 55
        elif char.realx > 2780 and char.realx < 2975:
            self.left, self.right = 2780 - Player.camerax + 32, 2975 - Player.camerax + 32
            if char == Player:
                Background.start = 2976
                Background.gap = 3000 - 2975
            return 2780 - Player.camerax + 32, 0, 2975 - Player.camerax + 32, 55
        elif char.realx > 3000 and char.realx < 4354:
            self.left, self.right = 3000 - Player.camerax + 32, 4354 - Player.camerax + 32
            if char == Player:
                Background.start = 4355
                Background.gap = 4378 - 4354
            return 3000 - Player.camerax + 32, 0, 4354 - Player.camerax + 32, 55
        elif char.realx > 4378:
            self.left, self.right = 0, 800
            return 0, 0, 800, 55
        else:
            self.left, self.right = Background.start, Background.start + Background.gap
            return Background.start - Player.camerax + 32, -200, Background.start + Background.gap - Player.camerax + 32, -200
