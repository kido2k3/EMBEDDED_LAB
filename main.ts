//  sender
radio.setGroup(5)
let received = 0
input.onGesture(Gesture.LogoUp, function on_gesture_logo_up() {
    
    received = 1
})
input.onGesture(Gesture.TiltLeft, function on_gesture_tilt_left() {
    
    received = 2
})
input.onGesture(Gesture.TiltRight, function on_gesture_tilt_right() {
    
    received = 3
})
input.onGesture(Gesture.LogoDown, function on_gesture_logo_down() {
    
    received = 4
})
let ack = 0
//  for testing
// if receivedNumber in [1, 2, 3, 4]:
//     radio.send_number(5)
radio.onReceivedNumber(function on_received_number(receivedNumber: number) {
    
    ack = receivedNumber
})
//  0: idle
//  1: send data
//  2: wait 2s for ack value. If no ack, resend data
//  resend over 2 times -> turn led(0, 0) on in 1s
//  received ack -> turn led(1, 1) on in 1s
let sender_st = 0
let timer_sender = 200
let send_time = 0
function send_data(data: number) {
    radio.sendNumber(data)
}

let led00_st = 0
let led00_timer = 100
let led11_st = 0
let led11_timer = 100
function fsm_sender() {
    
    
    if (sender_st == 0) {
        if (received) {
            sender_st = 1
            send_time = 0
        }
        
    } else if (sender_st == 1) {
        send_time += 1
        send_data(received)
        if (ack == 5) {
            received = 0
            sender_st = 0
            ack = 0
            led11_st = 1
        } else {
            timer_sender = 200
            sender_st = 2
        }
        
    } else if (sender_st == 2) {
        timer_sender -= 1
        if (ack == 5) {
            received = 0
            sender_st = 0
            ack = 0
            led11_st = 1
        } else if (timer_sender <= 0) {
            sender_st = 1
        } else if (send_time >= 3) {
            received = 0
            sender_st = 0
            led00_st = 1
        }
        
    }
    
    console.log(sender_st)
}

function fsm_led(led_st: number, led_timer: number, x: number, y: number): number[] {
    if (led_st == 1) {
        led.plot(x, y)
        led_timer -= 1
        if (led_timer <= 0) {
            led_st = 0
            led_timer = 100
        }
        
    } else if (led_st == 0) {
        led.unplot(x, y)
    }
    
    return [led_st, led_timer]
}

basic.forever(function on_forever() {
    
    fsm_sender()
    let ___tempvar4 = fsm_led(led00_st, led00_timer, 0, 0)
    led00_st = ___tempvar4[0]
    led00_timer = ___tempvar4[1]
    let ___tempvar5 = fsm_led(led11_st, led11_timer, 1, 1)
    led11_st = ___tempvar5[0]
    led11_timer = ___tempvar5[1]
    basic.pause(10)
})
