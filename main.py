
fsm_state = 0

list_icon = [
    IconNames.MEH, 
    IconNames.NO, 
    IconNames.PITCHFORK, 
    IconNames.QUARTER_NOTE,
    IconNames.RABBIT,
    IconNames.ROLLERSKATE,
    IconNames.SAD,
    IconNames.SCISSORS,
    IconNames.SILLY,
    IconNames.SKULL,
    IconNames.SMALL_DIAMOND,
    IconNames.SMALL_HEART,
    IconNames.SMALL_SQUARE,
    IconNames.SNAKE,
    IconNames.SQUARE,
    IconNames.STICK_FIGURE,
    IconNames.SURPRISED,
    IconNames.SWORD,
    IconNames.TSHIRT,
    IconNames.TARGET,
    IconNames.TORTOISE,
    IconNames.TRIANGLE,
    IconNames.UMBRELLA,
    IconNames.YES
    ]
def on_forever():
    for i in list_icon:
        basic.show_icon(i)
basic.forever(on_forever)
print(IconNames.TORTOISE)