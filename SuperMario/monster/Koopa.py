import random
import game_framework
from pico2d import *

PIXEL_PER_METER = 10.0 / 0.3
RUN_SPEED_KMPH = 5.0
RUN_SPEED_MPM = RUN_SPEED_KMPH * 1000.0 / 60.0
RUN_SPEED_MPS = RUN_SPEED_MPM / 60.0
RUN_SPEED_PPS = RUN_SPEED_MPS * PIXEL_PER_METER

TIME_PER_ACTION = 1
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
class WALK:
    def enter(self, event):
        pass

    def exit(self):
        pass

    def do(self):
        self.frame = (self.frame + ACTION_PER_TIME * self.clip * game_framework.frame_time) % self.clip  # 방향 전환 frame: 1
        if self.frame <= 1:
            self.frame = 2

        self.count_anim = 0

        self.x += self.x_dir * RUN_SPEED_PPS * game_framework.frame_time

    def draw(self):
        # self.image.clip_draw(int(self.frame) * 25, 50 * self.action, 25, 50, self.x, self.y)
        self.image.clip_composite_draw(int(self.frame) * 25, 50 * self.action, 25, 50, 0, self.reflect, self.x, self.y, 25, 50)


class RedKoopa:
    image = None

    def get_name(self):
        return 'monster'
    def __init__(self):
        if RedKoopa.image == None:
            RedKoopa.image = load_image('red_koopa.png')

        self.frame = 1
        self.x = random.randint(400, 3000)
        self.y = 100
        self.x_dir = -1
        self.action = 1
        self.clip = 17
        self.reflect = ' '
        self.cur_state = WALK
        self.cur_state.enter(self, None)

    def draw(self):
        self.cur_state.draw(self)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.cur_state.do(self)

    def get_bb(self):
        return self.x - 10, self.y - 23, self.x + 10, self.y + 21


class GreenKoopa:
    image = None

    def get_name(self):
        return 'monster'
    def __init__(self):
        if GreenKoopa.image == None:
            GreenKoopa.image = load_image('green_koopa.png')
        self.frame = 1
        self.action = 0
        self.x = random.randint(400, 3000)
        self.y = 100
        self.x_dir = -1
        self.action = 1
        self.reflect= ' '
        self.clip = 17

        self.TIME_PER_ACTION = 1
        self.ACTION_PER_TIME = 1.0 / self.TIME_PER_ACTION

        self.cur_state = WALK
        self.cur_state.enter(self, None)


    def draw(self):
        self.cur_state.draw(self)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.cur_state.do(self)

    def get_bb(self):
        return self.x - 10, self.y - 23, self.x + 10, self.y + 21



