import game_framework

from pico2d import *
import game_framework
import stage_state
import main_background
running = True
font = None
bgimg = None
logo = None
bx = None
ly = None
gap = None
voice = None
mainBgm = None
color = (255,255,255)
choose_sound = None
delay_draw = 0
def enter():

    global bx, ly, bgimg, font, logo, gap, voice, mainBgm, choose_sound
    bx = 3770
    ly = 430
    gap = 0.5
    font = load_font('./block/SuperMario256.ttf', 30)
    logo = load_image('./background/nsmb_logo.png')
    bgimg = main_background.BACKGROUND()
    mainBgm = load_music('./music/main_bgm.mp3')
    voice = load_wav('./music/Lets_Go.wav')
    choose_sound = load_wav('./music/Choose.wav')
    voice.set_volume(20)
    mainBgm.set_volume(30)
    choose_sound.set_volume(30)
    mainBgm.repeat_play()




def exit():
    global bgimg, font, voice, mainBgm
    del bgimg
    del font
    del voice
    del mainBgm

def update():
    global bx,ly,gap,delay_draw
    delay_draw += 1
    bx -= 1
    ly += gap
    ly = clamp(410,ly,430)
    bx = clamp(0, bx, 3770)
    if bx == 0:
        bx = 3770

    if ly == 410 or ly == 430:
        gap *= -1


    bgimg.edit_x(bx)
    delay(0.02)

pass
def draw():
    global  ly,delay_draw
    clear_canvas()
    bgimg.draw()
    if delay_draw % 2 == 0:
        font.draw(280, 100, 'Press SPACE', color)
    logo.clip_composite_draw(0,0, 2560, 1467, 0, ' ', 400, ly, 500, 300)

    update_canvas()
def handle_events():
    global color
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            choose_sound.play()
            voice.play()
            delay(1)
            game_framework.change_state(stage_state)



