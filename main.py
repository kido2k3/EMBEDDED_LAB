# sender
"""
0: idle
1: send data
2: wait 2s for ack value. If no ack, resend data
resend over 2 times -> turn led(0, 0) on in 1s
received ack -> turn led(1, 1) on in 1s
"""


def on_received_number(receivedNumber):
    global ack
    ack = receivedNumber
    # for testing
    if receivedNumber in [1, 2, 3, 4]:
        radio.send_number(5)
radio.on_received_number(on_received_number)

def sample_data():
    global tem_value, light_value
    tem_value = tem_value + input.temperature()
    light_value = light_value + input.light_level()
def send_data(data: number):
    radio.send_number(data)
def fsm_led(led_st: number, led_timer: number, x: number, y: number):
    if led_st == 1:
        led.plot(x, y)
        led_timer += 0 - 1
        if led_timer <= 0:
            led_st = 0
            led_timer = 100
    elif led_st == 0:
        led.unplot(x, y)
    return led_st, led_timer
def fsm_sender():
    global sender_st, send_time, received, ack, led11_st, timer_sender, led00_st
    if sender_st == 0:
        if received:
            sender_st = 1
            send_time = 0
    elif sender_st == 1:
        send_time += 1
        send_data(received)
        if ack == 5:
            received = 0
            sender_st = 0
            ack = 0
            led11_st = 1
        else:
            timer_sender = 200
            sender_st = 2
    elif sender_st == 2:
        timer_sender += 0 - 1
        if ack == 5:
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
cnt = 0
cur_st = 0
led00_st = 0
led11_st = 0
send_time = 0
received = 0
sender_st = 0
led_st2 = 0
led_timer2 = 0
light_value = 0
tem_value = 0
ack = 0
timer_sender = 0
TEM_THRESHOLD = 40
LIGHT_THRESHOLD = 200
radio.set_group(5)
timer_sender = 200
led00_timer = 100
led11_timer = 100

# 0: sample data
# 1: handle data and send signal
def on_forever():
    global cnt, cur_st, received, tem_value, light_value
    global led00_st, led00_timer, led11_st, led11_timer
    if cur_st == 0:
        sample_data()
        cnt = cnt + 1
        if cnt == 500:
            cnt = 0
            cur_st = 1
    elif cur_st == 1:
        tem_avg = tem_value / 500
        light_avg = light_value / 500
        if tem_avg > TEM_THRESHOLD:
            # heat warning
            received = 1
            print(1)
        else:
            received = 2
            print(2)
        if light_avg < LIGHT_THRESHOLD:
            # light warning
            received = 3
            print(3)
        else:
            received = 4
            print(4)
        cur_st = 0
        tem_value = 0
        light_value = 0
    fsm_sender()
    led00_st, led00_timer = fsm_led(led00_st, led00_timer, 0, 0)
    led11_st, led11_timer = fsm_led(led11_st, led11_timer, 1, 1)

    basic.pause(10)
basic.forever(on_forever)
