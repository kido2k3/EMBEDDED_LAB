
HEART_TIME = 2 #second

TIMER = 0.1
# 0: intial state
# 1: show heart in first 2 seconds
# 2: show firework 
cur_st = 0

cnt = 0

idx = 0
def display_fw(frame_num:int):
    if frame_num == 0:
        basic.show_leds("""
        .....
        .....
        .....
        .....
        ..#..
        """, 1
        )
    elif frame_num == 1:
        basic.show_leds("""
        .....
        .....
        .....
        ..#..
        .....
        """, 1
        )
    elif frame_num == 2:
        basic.show_leds("""
        .....
        .....
        ..#..
        .....
        .....
        """, 1
        )
    elif frame_num == 3:
        basic.show_leds("""
        .....
        ..#..
        .###.
        ..#..
        .....
        """, 1
        )
    elif frame_num == 4:
        basic.show_leds("""
        .#.#.
        #.#.#
        .###.
        #.#.#
        .#.#.
        """, 1
        )
    elif frame_num == 5:
        basic.show_leds("""
        .....
        .#.#.
        #.#.#
        .###.
        #####
        """, 1
        )
    elif frame_num == 6:
        basic.show_leds("""
        .....
        .....
        .#.#.
        #.#.#
        #####
        """, 1
        )
    elif frame_num == 7:
        basic.show_leds("""
        .....
        .....
        .....
        .#.#.
        #####
        """, 1
        )
    elif frame_num == 8:
        basic.show_leds("""
        .....
        .....
        .....
        .....
        #####
        """, 1
        )
def on_forever():
    global cur_st, cnt, idx
    # state machine
    if cur_st == 0:
        cnt = 0
        cur_st = 1
    elif cur_st == 1:
        basic.show_icon(IconNames.HEART, 1)
        cnt = cnt + 1
        if cnt == HEART_TIME * 100:
            cnt = 0
            idx = 0
            cur_st = 2
    elif cur_st == 2:
        display_fw(idx)
        cnt = cnt + 1
        if cnt == TIMER * 100:
            cnt = 0
            idx = idx + 1
            if idx == 9:
                idx = 0
    basic.pause(1)
basic.forever(on_forever)
