let data = 0
function sample_data() {
    
    data = data + input.compassHeading()
}

function display_arrow(value: number) {
    if (value < 45) {
        basic.showArrow(ArrowNames.North, 1)
    } else if (value < 135) {
        basic.showArrow(ArrowNames.West, 1)
    } else if (value < 225) {
        basic.showArrow(ArrowNames.South, 1)
    } else if (value < 315) {
        basic.showArrow(ArrowNames.East, 1)
    } else if (value < 359) {
        basic.showArrow(ArrowNames.North, 1)
    }
    
}

let cnt = 0
basic.forever(function on_forever() {
    
    sample_data()
    cnt = cnt + 1
    if (cnt == 10) {
        cnt = 0
        display_arrow(data / 10)
        data = 0
    }
    
    basic.pause(10)
})
