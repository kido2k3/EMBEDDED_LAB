//  sender
/** 
0: idle
1: send data
2: wait 2s for ack value. If no ack, resend data
resend over 2 times -> turn led(0, 0) on in 1s
received ack -> turn led(1, 1) on in 1s

 */
radio.onReceivedNumber(function on_received_number(receivedNumber: number) {
    
    ack = receivedNumber
    //  for testing
    if ([1, 2, 3, 4].indexOf(receivedNumber) >= 0) {
        radio.sendNumber(5)
    }
    
})
function sample_data() {
    
    tem_value = tem_value + input.temperature()
    light_value = light_value + input.lightLevel()
}

function send_data(data: number) {
    radio.sendNumber(data)
}

function fsm_led(led_st: number, led_timer: number, x: number, y: number): number[] {
    if (led_st == 1) {
        led.plot(x, y)
        led_timer += 0 - 1
        if (led_timer <= 0) {
            led_st = 0
            led_timer = 100
        }
        
    } else if (led_st == 0) {
        led.unplot(x, y)
    }
    
    return [led_st, led_timer]
}

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
        timer_sender += 0 - 1
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
    
}

let cnt = 0
let cur_st = 0
let led00_st = 0
let led11_st = 0
let send_time = 0
let received = 0
let sender_st = 0
let led_st2 = 0
let led_timer2 = 0
let light_value = 0
let tem_value = 0
let ack = 0
let timer_sender = 0
let TEM_THRESHOLD = 40
let LIGHT_THRESHOLD = 200
radio.setGroup(5)
timer_sender = 200
let led00_timer = 100
let led11_timer = 100
//  0: sample data
//  1: handle data and send signal
basic.forever(function on_forever() {
    let tem_avg: number;
    let light_avg: number;
    
    
    if (cur_st == 0) {
        sample_data()
        cnt = cnt + 1
        if (cnt == 500) {
            cnt = 0
            cur_st = 1
        }
        
    } else if (cur_st == 1) {
        tem_avg = tem_value / 500
        light_avg = light_value / 500
        if (tem_avg > TEM_THRESHOLD) {
            //  heat warning
            received = 1
            console.log(1)
        } else {
            received = 2
            console.log(2)
        }
        
        if (light_avg < LIGHT_THRESHOLD) {
            //  light warning
            received = 3
            console.log(3)
        } else {
            received = 4
            console.log(4)
        }
        
        cur_st = 0
        tem_value = 0
        light_value = 0
    }
    
    fsm_sender()
    let ___tempvar4 = fsm_led(led00_st, led00_timer, 0, 0)
    led00_st = ___tempvar4[0]
    led00_timer = ___tempvar4[1]
    let ___tempvar5 = fsm_led(led11_st, led11_timer, 1, 1)
    led11_st = ___tempvar5[0]
    led11_timer = ___tempvar5[1]
    basic.pause(10)
})
