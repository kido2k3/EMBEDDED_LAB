input.onGesture(Gesture.LogoUp, function () {
    radio.sendNumber(2)
})
input.onGesture(Gesture.TiltLeft, function () {
    radio.sendNumber(0)
})
input.onGesture(Gesture.TiltRight, function () {
    radio.sendNumber(1)
})
input.onGesture(Gesture.LogoDown, function () {
    radio.sendNumber(3)
})
radio.setGroup(5)
basic.forever(function () {
    basic.showString("Sender")
})
