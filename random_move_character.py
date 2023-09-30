from pico2d import *
import random # randint 함수 사용

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
TUK_ground = load_image('TUK_GROUND.png')
char = load_image('animation_sheet.png')
cursor = load_image('hand_arrow.png')

def handle_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
hide_cursor()
frame = 0

def linear_move(pt1,pt2): # 랜덤 위치를 지정 할 함수
    global frame

    x1, y1 = pt1[0], pt1[1]
    x2, y2 = pt2[0], pt2[1]

    for n in range(0, 100+1,10):

        t = n / 100
        x = (1 - t) * x1 + t * x2
        y = (1 - t) * y1 + t * y2

        clear_canvas()
        cursor.draw(x1, x1)
        TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
        char.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        frame = (frame + 1) % 8
        delay(0.05)
        update_canvas()
        handle_events()

pass


points = [(random.randint(0,TUK_WIDTH), random.randint(0,TUK_HEIGHT)) for n in range(100)]
# TUK_GROUND 내 좌표 랜덤 생성

for n in range(0,100+1):
    linear_move(points[n],points[n+1])

close_canvas()