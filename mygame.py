import platform
import os

if platform.architecture()[0] == '32bit':
    os.environ["PYSDL2_DLL_PATH"] = "./SDL2/x86"
else:
    os.environ["PYSDL2_DLL_PATH"] = "./SDL2/x64"

from pico2d import *

import game_framework
import title_state


CLIENT_WIDTH = 480
CLIENT_HEIGHT = 420

open_canvas(CLIENT_WIDTH, CLIENT_HEIGHT)
game_framework.run(title_state)
close_canvas()