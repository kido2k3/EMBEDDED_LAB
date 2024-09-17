
def display_lArrow(framenum: any):
    if framenum == 0:
        basic.show_leds("""
            .....
            .....
            ....#
            .....
            .....
            """, 1)
    elif framenum == 1:
        basic.show_leds("""
            .....
            ....#
            ...##
            ....#
            .....
            """, 1)
    elif framenum == 2:
        basic.show_leds("""
            ....#
            ...#.
            ..###
            ...#.
            ....#
            """, 1)
    elif framenum == 3:
        basic.show_leds("""
            ...#.
            ..#..
            .####
            ..#..
            ...#.
            """, 1)
    elif framenum == 4:
        basic.show_leds("""
            ..#..
            .#...
            #####
            .#...
            ..#..
            """, 1)
    elif framenum == 5:
        basic.show_leds("""
            .#...
            #....
            ####.
            #....
            .#...
            """, 1)
    elif framenum == 6:
        basic.show_leds("""
            #....
            .....
            ###..
            .....
            #....
            """, 1)
    elif framenum == 7:
        basic.show_leds("""
            .....
            .....
            ##...
            .....
            .....
            """, 1)
    elif framenum == 8:
        basic.show_leds("""
            .....
            .....
            #....
            .....
            .....
            """, 1)
def display_rArrow(framenum2: any):
    if framenum2 == 0:
        basic.show_leds("""
            .....
            .....
            #....
            .....
            .....
            """, 1)
    elif framenum2 == 1:
        basic.show_leds("""
            .....
            #....
            ##...
            #....
            .....
            """, 1)
    elif framenum2 == 2:
        basic.show_leds("""
            #....
            .#...
            ###..
            .#...
            #....
            """, 1)
    elif framenum2 == 3:
        basic.show_leds("""
            .#...
            ..#..
            ####.
            ..#..
            .#...
            """, 1)
    elif framenum2 == 4:
        basic.show_leds("""
            ..#..
            ...#.
            #####
            ...#.
            ..#..
            """, 1)
    elif framenum2 == 5:
        basic.show_leds("""
            ...#.
            ....#
            .####
            ....#
            ...#.
            """, 1)
    elif framenum2 == 6:
        basic.show_leds("""
            ....#
            .....
            ..###
            .....
            ....#
            """, 1)
    elif framenum2 == 7:
        basic.show_leds("""
            .....
            .....
            ...##
            .....
            .....
            """, 1)
    elif framenum2 == 8:
        basic.show_leds("""
            .....
            .....
            ....#
            .....
            .....
            """, 1)


# 0: left arrow
# 1: right arrow
cur_st = 0
idx = 0
cnt = 0
def on_gesture_tilt_left():
    global cur_st, idx
    cur_st = 0
    idx = 0
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def on_gesture_tilt_right():
    global cur_st, idx
    cur_st = 1
    idx = 0
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)
def on_forever():
    global cur_st, idx, cnt
    if cur_st == 0:
        display_lArrow(idx)
    elif cur_st == 1:
        display_rArrow(idx)
    cnt = cnt + 1
    if cnt == 10:
        cnt = 0
        idx = idx + 1
        if idx == 9:
            idx = 0
    basic.pause(10)
basic.forever(on_forever)
