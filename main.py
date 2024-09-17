def on_gesture_logo_up():
    radio.send_number(2)
input.on_gesture(Gesture.LOGO_UP, on_gesture_logo_up)

def on_gesture_tilt_left():
    radio.send_number(0)
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def on_gesture_tilt_right():
    radio.send_number(1)
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

def on_gesture_logo_down():
    radio.send_number(3)
input.on_gesture(Gesture.LOGO_DOWN, on_gesture_logo_down)

radio.set_group(5)

def on_forever():
    basic.show_string("Sender")
basic.forever(on_forever)
