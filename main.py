# receiver
radio.set_group(5)

def toggle_led():
    for i in range(3):
        led.toggle(0, i)
    led.toggle(0, 4)

heat_timer = 0
heat_st = 0
def heat_warning_fsm(cur_st: int):
    global heat_timer
    if cur_st == 0:
        for i in range(3):
            led.unplot(0, i)
        led.unplot(0, 4)
        heat_timer = 0
    elif cur_st == 1:
        heat_timer = heat_timer + 1
        if heat_timer == 25:
            toggle_led()
            heat_timer = 0

def light_off():
    for i in range(2, 5):
        for j in range(2, 5):
            led.unplot(i, j)
def light_on():
    for i in range(2, 5):
        for j in range(2, 5):
            led.plot(i, j)
light_st = 0
def light_warning_fsm(cur_st: int):
    if cur_st == 0:
        light_off()
    elif cur_st == 1:
        light_on()
def on_received_number(receivedNumber):
    global heat_st, light_st
    if receivedNumber == 1:
        heat_st = 1
    elif receivedNumber == 2:
        heat_st = 0
    elif receivedNumber == 4:
        light_st = 0
    elif receivedNumber == 3:
        light_st = 1
    if receivedNumber in [1, 2, 3, 4]:
        radio.send_number(5)
radio.on_received_number(on_received_number)

def on_forever():
    global heat_st, light_st
    heat_warning_fsm(heat_st)
    light_warning_fsm(light_st)
    basic.pause(10)
basic.forever(on_forever)

# for demo
def on_button_pressed_a():
    # heat warning
    radio.send_number(1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    # heat normal
    radio.send_number(2)
input.on_button_pressed(Button.B, on_button_pressed_b)
def on_button_pressed_ab():
    # light warning
    radio.send_number(3)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_logo_event_pressed():
    # light normal
    radio.send_number(4)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_event_pressed)