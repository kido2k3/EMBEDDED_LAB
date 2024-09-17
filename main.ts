let fsm_state = 0
let list_icon = [IconNames.Meh, IconNames.No, IconNames.Pitchfork, IconNames.QuarterNote, IconNames.Rabbit, IconNames.Rollerskate, IconNames.Sad, IconNames.Scissors, IconNames.Silly, IconNames.Skull, IconNames.SmallDiamond, IconNames.SmallHeart, IconNames.SmallSquare, IconNames.Snake, IconNames.Square, IconNames.StickFigure, IconNames.Surprised, IconNames.Sword, IconNames.TShirt, IconNames.Target, IconNames.Tortoise, IconNames.Triangle, IconNames.Umbrella, IconNames.Yes]
basic.forever(function on_forever() {
    for (let i of list_icon) {
        basic.showIcon(i)
    }
})
console.log(IconNames.Tortoise)
