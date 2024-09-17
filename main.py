def clear_led():
    for i in range(5):
        led.unplot(i, 4)
class boat:
    x = 2
    y = 4
    def show_boat(self):
        clear_led()
        led.plot(self.x, self.y)
    def go_left(self):
        if self.x > 0:
            self.x = self.x - 1
    def go_right(self):
        if self.x < 4:
            self.x = self.x + 1
cnt = 0
myBoat = boat()
def on_forever():
    global myBoat, cnt
    myBoat.show_boat()
    if input.button_is_pressed(Button.B):
        cnt = cnt + 1
    elif input.button_is_pressed(Button.A):
        cnt = cnt - 1
    else:
        cnt = 0
    if cnt == 1:
        myBoat.go_right()
    
    if cnt == -1:
        myBoat.go_left()
    basic.pause(10)
basic.forever(on_forever)
