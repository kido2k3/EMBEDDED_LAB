dataX = 0
dataY = 0
dataZ = 0

def on_gesture_tilt_left():
    basic.show_arrow(ArrowNames.WEST)
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def on_gesture_tilt_right():
    basic.show_arrow(ArrowNames.EAST)
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

def on_forever():
    global dataX, dataY, dataZ
    dataX = input.acceleration(Dimension.X)
    dataY = input.acceleration(Dimension.Y)
    dataZ = input.acceleration(Dimension.Z)
basic.forever(on_forever)
