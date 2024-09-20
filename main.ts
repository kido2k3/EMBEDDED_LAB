//  receiver
radio.setGroup(5)
let flag = 0
let buf = 1
radio.onReceivedNumber(function on_received_number(receivedNumber: number) {
    
    flag = 1
    buf = receivedNumber
    if ([1, 2, 3, 4].indexOf(buf) >= 0) {
        radio.sendNumber(5)
    }
    
})
basic.forever(function on_forever() {
    
    if (flag == 1) {
        flag = 0
        if (buf == 3) {
            basic.showArrow(ArrowNames.West)
        } else if (buf == 2) {
            basic.showArrow(ArrowNames.East)
        } else if (buf == 4) {
            basic.showArrow(ArrowNames.South)
        } else if (buf == 1) {
            basic.showArrow(ArrowNames.North)
        }
        
    }
    
    basic.pause(10)
})
//  for testing
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    //  up
    radio.sendNumber(1)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    //  left
    radio.sendNumber(2)
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    //  right
    radio.sendNumber(3)
})
input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_event_pressed() {
    //  down
    radio.sendNumber(4)
})
