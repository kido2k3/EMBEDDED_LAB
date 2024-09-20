//  receiver
radio.setGroup(5)
function toggle_led() {
    for (let i = 0; i < 3; i++) {
        led.toggle(0, i)
    }
    led.toggle(0, 4)
}

let heat_timer = 0
let heat_st = 0
function heat_warning_fsm(cur_st: number) {
    
    if (cur_st == 0) {
        for (let i = 0; i < 3; i++) {
            led.unplot(0, i)
        }
        led.unplot(0, 4)
        heat_timer = 0
    } else if (cur_st == 1) {
        heat_timer = heat_timer + 1
        if (heat_timer == 25) {
            toggle_led()
            heat_timer = 0
        }
        
    }
    
}

function light_off() {
    for (let i = 2; i < 5; i++) {
        for (let j = 2; j < 5; j++) {
            led.unplot(i, j)
        }
    }
}

function light_on() {
    for (let i = 2; i < 5; i++) {
        for (let j = 2; j < 5; j++) {
            led.plot(i, j)
        }
    }
}

let light_st = 0
function light_warning_fsm(cur_st: number) {
    if (cur_st == 0) {
        light_off()
    } else if (cur_st == 1) {
        light_on()
    }
    
}

radio.onReceivedNumber(function on_received_number(receivedNumber: number) {
    
    if (receivedNumber == 1) {
        heat_st = 1
    } else if (receivedNumber == 2) {
        heat_st = 0
    } else if (receivedNumber == 4) {
        light_st = 0
    } else if (receivedNumber == 3) {
        light_st = 1
    }
    
    if ([1, 2, 3, 4].indexOf(receivedNumber) >= 0) {
        radio.sendNumber(5)
    }
    
})
basic.forever(function on_forever() {
    
    heat_warning_fsm(heat_st)
    light_warning_fsm(light_st)
    basic.pause(10)
})
//  for demo
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    //  heat warning
    radio.sendNumber(1)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    //  heat normal
    radio.sendNumber(2)
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    //  light warning
    radio.sendNumber(3)
})
input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_event_pressed() {
    //  light normal
    radio.sendNumber(4)
})
