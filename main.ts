let dataX = 0
let dataY = 0
let dataZ = 0
input.onGesture(Gesture.TiltLeft, function on_gesture_tilt_left() {
    basic.showArrow(ArrowNames.West)
})
input.onGesture(Gesture.TiltRight, function on_gesture_tilt_right() {
    basic.showArrow(ArrowNames.East)
})
basic.forever(function on_forever() {
    
    dataX = input.acceleration(Dimension.X)
    dataY = input.acceleration(Dimension.Y)
    dataZ = input.acceleration(Dimension.Z)
})
