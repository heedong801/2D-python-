import game_framework
import main_state
from pico2d import *

name = "EndState"
image = None

def enter():
    global image
    image = load_image('end.png')

def exit():
    global image
    del(image)

def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if( event.type == SDL_KEYDOWN ):
                if( event.key == SDLK_ESCAPE):
                    game_framework.quit()

def draw(frame_time):
    clear_canvas()
    image.draw(240, 210)
    update_canvas()

def update(frame_time):
    pass

def pause():
    pass

def resume():
    pass






