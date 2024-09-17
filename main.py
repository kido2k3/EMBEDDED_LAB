
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
def on_forever():
    global cur_st, idx, cnt
    if cur_st == 0:
        display_lArrow(idx)
        if input.button_is_pressed(Button.B):
            cur_st = 1
            idx = 0
    elif cur_st == 1:
        display_rArrow(idx)
        if input.button_is_pressed(Button.A):
            cur_st = 0
            idx = 0
    cnt = cnt + 1
    if cnt == 10:
        cnt = 0
        idx = idx + 1
        if idx == 9:
            idx = 0
    basic.pause(10)
basic.forever(on_forever)
