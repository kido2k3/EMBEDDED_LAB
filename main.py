data = 0
def sample_data():
    global data
    data = data + input.compass_heading()

def display_arrow(value: float):
    if value < 45:
        basic.show_arrow(ArrowNames.NORTH, 1)
    elif value < 135:
        basic.show_arrow(ArrowNames.WEST, 1)
    elif value < 225:
        basic.show_arrow(ArrowNames.SOUTH, 1)
    elif value < 315:
        basic.show_arrow(ArrowNames.EAST, 1)
    elif value < 359:
        basic.show_arrow(ArrowNames.NORTH, 1)


cnt = 0
def on_forever():
    global data, cnt
    sample_data()
    cnt = cnt + 1
    if cnt == 10:
        cnt = 0
        display_arrow(data / 10)
        data = 0
    basic.pause(10)
basic.forever(on_forever)
