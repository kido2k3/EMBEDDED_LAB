# receiver
radio.set_group(5)

flag = 0
buf = 1
def on_received_number(receivedNumber):
    global flag, buf
    flag = 1
    buf = receivedNumber
    if buf in [1, 2, 3, 4]:
        radio.send_number(5)
radio.on_received_number(on_received_number)


def on_forever():
    global flag, buf
    if flag == 1:
        flag = 0
        if buf == 3:
            basic.show_arrow(ArrowNames.WEST)
        elif buf == 2:
            basic.show_arrow(ArrowNames.EAST)
        elif buf == 4:
            basic.show_arrow(ArrowNames.SOUTH)
        elif buf == 1:
            basic.show_arrow(ArrowNames.NORTH)
    basic.pause(10)
basic.forever(on_forever)

# for testing
def on_button_pressed_a():
    # up
    radio.send_number(1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    # left
    radio.send_number(2)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_button_pressed_ab():
    # right
    radio.send_number(3)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_logo_event_pressed():
    # down
    radio.send_number(4)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_event_pressed)