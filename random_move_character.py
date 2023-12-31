from pico2d import *
import random # randint 함수 사용

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
TUK_ground = load_image('TUK_GROUND.png')
char = load_image('animation_sheet.png')
cursor = load_image('hand_arrow.png')

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
            exit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
            exit()

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
hide_cursor()
frame = 0
frame2 = 0

def linear_move(pt1,pt2): # 랜덤 위치를 지정 할 함수
    global frame, frame2

    x1, y1 = pt1[0], pt1[1]
    x2, y2 = pt2[0], pt2[1]


    for n in range(0, 100+1,5):

        t = n / 100
        x = (1 - t) * x1 + t * x2
        y = (1 - t) * y1 + t * y2

        clear_canvas()
        TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
        cursor.draw(x2, y2)

        if x1 > x2: # 왼쪽으로 이동할 때 char.clip_draw 함수 내의 y좌표 조정
            frame2 = 0
        else:
            frame2 = 1

        char.clip_draw(frame * 100, frame2 * 100, 100, 100, x, y)
        frame = (frame + 1) % 8
        frame2 = (frame2 + 1) % 8
        delay(0.05)
        update_canvas()
        handle_events()

points = [(random.randint(0,TUK_WIDTH), random.randint(0,TUK_HEIGHT)) for n in range(100)]
# TUK_GROUND 내 좌표 랜덤 생성

for n in range(0,100):
    linear_move(points[n],points[n+1])

close_canvas()