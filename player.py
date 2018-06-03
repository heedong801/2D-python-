from pico2d import *

jumpnum = 0
jumpY = 95
jump = False

class Player:
    image = None
    RIGHT_STAND, RIGHT_RUN, RIGHT_JUMPUP, RIGHT_JUMPDOWN, RIGHT_DIE, LEFT_STAND, LEFT_RUN, LEFT_JUMPUP, LEFT_JUMPDOWN, LEFT_DIE = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPEED_KMPH = 20.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    JUMP_SPEED_KMPH = 30.0
    JUMP_SPEED_MPM = (JUMP_SPEED_KMPH * 1000.0 / 60.0)
    JUMP_SPEED_MPS = (JUMP_SPEED_MPM / 60.0)
    JUMP_SPEED_PPS = (JUMP_SPEED_MPS * PIXEL_PER_METER)

    die = False
    Left_push = False
    Right_push = False
    distance = 0
    camerax = 40
    realx = 40
    realy = 75
    mob1speedup = False
    moveableL = True
    moveableR = True
    jumpable = True

    muscleman = False
    status = 0

    jump_sound = None
    powerup_sound = None
    death_sound = None

    def __init__(self):
        self.x, self.y = 40, 75
        self.top, self.bottom = 0, 0
        self.left, self.right = 0, 0
        self.frame = 0
        self.xdir, self.ydir = 0, 0
        self.direction = self.RIGHT_STAND
        self.Jump_state = False
        if Player.powerup_sound == None:
            Player.powerup_sound = load_wav('powerup.wav')
        if Player.death_sound == None:
            Player.death_sound = load_wav('death.wav')
        Player.death_sound.set_volume(64)
        Player.powerup_sound.set_volume(32)
        if Player.image == None:
            Player.image = load_image('player.png')

    def set_background(self, bg):
        self.bg = bg

    def get_xy(self):
        return Player.realx + 45, self.y

    def update(self, frame_time):
        global jumpnum, jumpY, jump
        print(Player.realx)
        Player.status = self.direction
        Player.realy = self.y

        Player.distance = Player.RUN_SPEED_PPS * frame_time
        Jumpdistance = Player.JUMP_SPEED_PPS * frame_time

        if not Player.die and not Player.muscleman:
            if self.Jump_state == False:
                jumpnum = 0
                if self.direction == self.LEFT_JUMPDOWN:
                    if Player.Left_push == 0 :
                        self.direction = self.LEFT_STAND
                    else:
                        self.direction = self.LEFT_RUN
                elif self.direction == self.RIGHT_JUMPDOWN:
                    if Player.Right_push == 0:
                        self.direction = self.RIGHT_STAND
                    else:
                        self.direction = self.RIGHT_RUN

            if self.direction in ( self.RIGHT_JUMPUP, self.LEFT_JUMPUP):
                self.ydir = 1
            elif self.direction in ( self.RIGHT_JUMPDOWN, self.LEFT_JUMPDOWN):
                self.ydir = -1

            self.x = clamp(0, self.x, self.bg.w)

            if Player.moveableR:
                if self.direction in (self.RIGHT_RUN, self.RIGHT_JUMPUP, self.RIGHT_JUMPDOWN):
                    if Player.Right_push == True:
                        if self.x < 200:
                            self.x += (self.xdir * Player.distance)
                            Player.realx += Player.distance
                            Player.mob1speedup = False
                        else:
                            Player.mob1speedup = True
                            if self.realx > 4432:
                                pass
                            elif self.realx > 4157:
                                self.x += (self.xdir * Player.distance)
                                Player.realx += Player.distance
                            else:
                                Player.camerax += Player.distance
                                Player.realx += Player.distance
            if Player.moveableL:
                if self.direction in (self.LEFT_RUN, self.LEFT_JUMPUP, self.LEFT_JUMPDOWN):
                    if Player.Left_push == True:
                        if self.x > 15:
                            self.x += (self.xdir * Player.distance)
                            Player.realx += (self.xdir * Player.distance)

            if self.Jump_state == True:
                if self.direction in ( self.RIGHT_JUMPUP, self.LEFT_JUMPUP):
                    if jumpnum < jumpY:
                        self.y += (self.ydir * Jumpdistance)
                        jumpnum += Player.distance
                    else:
                        if self.direction == self.RIGHT_JUMPUP:
                            self.direction = self.RIGHT_JUMPDOWN
                        elif self.direction == self.LEFT_JUMPUP:
                            self.direction = self.LEFT_JUMPDOWN
                        jumpnum = 0
        else:
            if Player.muscleman == False:
                if self.direction in ( self.RIGHT_JUMPDOWN, self.RIGHT_JUMPUP, self.RIGHT_RUN, self.RIGHT_STAND):
                    self.direction = self.RIGHT_DIE
                elif self.direction in ( self.LEFT_JUMPDOWN, self.LEFT_JUMPUP, self.LEFT_RUN, self.LEFT_STAND):
                    self.direction = self.LEFT_DIE

                if jumpnum < jumpY:
                    self.y += Jumpdistance
                    jumpnum += Player.distance
                else:
                    jump = True

                if jump == True:
                    self.y += (-1)* Jumpdistance
                    if self.y < -50:
                        jump = False


        if self.y < 0 :
            if Player.die == False:
                Player.die = True
                Player.death_sound.play()

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        self.top = self.y + 20
        self.bottom = self.y - 20 + 1
        if self.direction in ( self.RIGHT_JUMPUP, self.LEFT_JUMPUP, self.RIGHT_JUMPDOWN, self.LEFT_JUMPDOWN):
            self.left = self.x - 10
            self.right = self.x + 15
            return self.x - 10, self.y - 20, self.x + 15, self.y + 20
        if self.direction in ( self.RIGHT_RUN, self.LEFT_RUN):
            self.left = self.x - 15
            self.right = self.x + 12
            return self.x - 15, self.y - 20, self.x + 12, self.y + 20
        else:
            self.left = self.x - 15
            self.right = self.x + 7
            return self.x - 15, self.y - 20, self.x + 7, self.y + 20

    def handle_event(self, event):
        if Player.die == False:
            if event.type == SDL_KEYDOWN:
                if event.key == SDLK_LEFT:
                     self.frame = 1
                     self.xdir = -1
                     Player.Right_push = False
                     Player.Left_push = True
                     if self.direction in (self.RIGHT_STAND, self.RIGHT_RUN, self.LEFT_STAND):
                         self.direction = self.LEFT_RUN
                     elif self.direction == self.RIGHT_JUMPUP:
                         self.direction = self.LEFT_JUMPUP
                     elif self.direction == self.RIGHT_JUMPDOWN:
                         self.direction = self.LEFT_JUMPDOWN

                elif event.key == SDLK_RIGHT:
                    Player.Right_push = True
                    Player.Left_push  = False
                    self.xdir = 1
                    self.frame = 0
                    if self.direction in (self.RIGHT_STAND, self.LEFT_RUN, self.LEFT_STAND):
                        self.direction = self.RIGHT_RUN
                    elif self.direction == self.LEFT_JUMPUP:
                        self.direction = self.RIGHT_JUMPUP
                    elif self.direction == self.LEFT_JUMPDOWN:
                        self.direction = self.RIGHT_JUMPDOWN

                elif event.key == SDLK_UP:
                    if self.Jump_state == False and Player.jumpable == True:
                     self.Jump_state = True

                     if self.direction in (self.RIGHT_STAND, self.RIGHT_RUN):
                         self.direction = self.RIGHT_JUMPUP
                     elif self.direction in (self.LEFT_STAND, self.LEFT_RUN):
                         self.direction = self.LEFT_JUMPUP

            elif event.type == SDL_KEYUP:
                if event.key == SDLK_LEFT:
                     Player.Left_push = False
                     if self.direction == self.LEFT_RUN:
                         self.direction = self.LEFT_STAND
                         self.xdir = 0
                elif event.key == SDLK_RIGHT:
                    Player.Right_push = False
                    if self.direction== self.RIGHT_RUN:
                        self.direction = self.RIGHT_STAND
                        self.xdir = 0



    def draw(self, frame_time):
        if self.frame == 1:
            if self.direction in (self.LEFT_JUMPDOWN, self.LEFT_DIE):
                self.image.clip_draw((self.direction - 6) * 28, self.frame * 35, 28, 35, self.x, self.y)
            else:
                self.image.clip_draw((self.direction - 5 ) * 28, self.frame * 35, 28, 35, self.x, self.y)
        else:
            if self.direction in (self.RIGHT_JUMPDOWN, self.RIGHT_DIE):
                self.image.clip_draw((self.direction - 1) * 28, self.frame * 35, 28, 35, self.x, self.y)
            else:
                self.image.clip_draw(self.direction * 28, self.frame * 35, 28, 35, self.x, self.y)

