def on_gesture_logo_up():
    global cur_st
    cur_st = 1
input.on_gesture(Gesture.LOGO_UP, on_gesture_logo_up)

def on_gesture_tilt_left():
    global cur_st
    cur_st = 3
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def on_gesture_tilt_right():
    global cur_st
    cur_st = 4
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

def on_gesture_logo_down():
    global cur_st
    cur_st = 2
input.on_gesture(Gesture.LOGO_DOWN, on_gesture_logo_down)

cur_st = 0
cur_st = 1

def on_forever():
    basic.show_number(cur_st)
basic.forever(on_forever)
