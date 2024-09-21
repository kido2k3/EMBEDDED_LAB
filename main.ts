input.onGesture(Gesture.LogoUp, function on_gesture_logo_up() {
    
    cur_st = 1
})
input.onGesture(Gesture.TiltLeft, function on_gesture_tilt_left() {
    
    cur_st = 3
})
input.onGesture(Gesture.TiltRight, function on_gesture_tilt_right() {
    
    cur_st = 4
})
input.onGesture(Gesture.LogoDown, function on_gesture_logo_down() {
    
    cur_st = 2
})
let cur_st = 1
basic.forever(function on_forever() {
    basic.showNumber(cur_st, 1)
})
