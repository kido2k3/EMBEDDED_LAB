# sender
radio.set_group(5)

received = 0
def on_gesture_logo_up():
    global received
    received = 1
input.on_gesture(Gesture.LOGO_UP, on_gesture_logo_up)

def on_gesture_tilt_left():
    global received
    received = 2
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def on_gesture_tilt_right():
    global received
    received = 3
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

def on_gesture_logo_down():
    global received
    received = 4
input.on_gesture(Gesture.LOGO_DOWN, on_gesture_logo_down)



ack = 0
def on_received_number(receivedNumber):
    global ack
    ack = receivedNumber
    # for testing
    #radio.send_number(ack)
radio.on_received_number(on_received_number)

# 0: idle
# 1: send data
# 2: wait 2s for ack value. If no ack, resend data
# resend over 2 times -> turn led(0, 0) on in 1s
# received ack -> turn led(1, 1) on in 1s
sender_st = 0
timer_sender = 200
send_time = 0
def send_data(data: int):
    radio.send_number(data)

led00_st = 0
led00_timer = 100
led11_st = 0
led11_timer = 100

def fsm_sender():
    global sender_st, received, send_time, timer_sender, ack
    global led00_st, led11_st
    if sender_st == 0:
        if received:
            sender_st = 1
            send_time = 0
    elif sender_st == 1:
        send_time += 1
        send_data(received)
        if received == ack:
            received = 0
            sender_st = 0
            ack = 0
            led11_st = 1
        else:
            timer_sender = 200
            sender_st = 2
    elif sender_st == 2:
        timer_sender -= 1
        if received == ack:
            received = 0
            sender_st = 0
            ack = 0
            led11_st = 1
        elif timer_sender <= 0:
            sender_st = 1
        elif send_time >= 3:
            received = 0
            sender_st = 0
            led00_st = 1
    print(sender_st)
def fsm_led(led_st, led_timer, x, y):
    if led_st == 1:
        led.plot(x, y)
        led_timer -= 1
        if led_timer <= 0:
            led_st = 0
            led_timer = 100
    elif led_st == 0:
        led.unplot(x, y)
    return led_st, led_timer
       
def on_forever():
    global led00_st, led00_timer, led11_st, led11_timer
    fsm_sender() 

    led00_st, led00_timer = fsm_led(led00_st, led00_timer, 0, 0)
    
    led11_st, led11_timer = fsm_led(led11_st, led11_timer, 1, 1)
    basic.pause(10)
basic.forever(on_forever)