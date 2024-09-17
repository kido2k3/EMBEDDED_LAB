radio.set_group(5)
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

# receiver
flag = 0
buf = 1
def on_received_number(receivedNumber):
    global flag, buf
    flag = 1
    buf = receivedNumber
radio.on_received_number(on_received_number)


def on_forever():
    global flag, buf
    if flag == 1:
        flag = 0
        if buf == 0:
            basic.show_arrow(ArrowNames.WEST)
        elif buf == 1:
            basic.show_arrow(ArrowNames.EAST)
        elif buf == 2:
            basic.show_arrow(ArrowNames.SOUTH)
        elif buf == 3:
            basic.show_arrow(ArrowNames.NORTH)
    basic.pause(10)
basic.forever(on_forever)

