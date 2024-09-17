radio.setGroup(5)
input.onGesture(Gesture.LogoUp, function on_gesture_logo_up() {
    radio.sendNumber(2)
})
input.onGesture(Gesture.TiltLeft, function on_gesture_tilt_left() {
    radio.sendNumber(0)
})
input.onGesture(Gesture.TiltRight, function on_gesture_tilt_right() {
    radio.sendNumber(1)
})
input.onGesture(Gesture.LogoDown, function on_gesture_logo_down() {
    radio.sendNumber(3)
})
//  receiver
let flag = 0
let buf = 1
radio.onReceivedNumber(function on_received_number(receivedNumber: number) {
    
    flag = 1
    buf = receivedNumber
})
basic.forever(function on_forever() {
    
    if (flag == 1) {
        flag = 0
        if (buf == 0) {
            basic.showArrow(ArrowNames.West)
        } else if (buf == 1) {
            basic.showArrow(ArrowNames.East)
        } else if (buf == 2) {
            basic.showArrow(ArrowNames.South)
        } else if (buf == 3) {
            basic.showArrow(ArrowNames.North)
        }
        
    }
    
    basic.pause(10)
})
