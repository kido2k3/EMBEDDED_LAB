function clear_led() {
    for (let i = 0; i < 5; i++) {
        led.unplot(i, 4)
    }
}

class boat {
    static x: number
    private ___x_is_set: boolean
    private ___x: number
    get x(): number {
        return this.___x_is_set ? this.___x : boat.x
    }
    set x(value: number) {
        this.___x_is_set = true
        this.___x = value
    }
    
    static y: number
    private ___y_is_set: boolean
    private ___y: number
    get y(): number {
        return this.___y_is_set ? this.___y : boat.y
    }
    set y(value: number) {
        this.___y_is_set = true
        this.___y = value
    }
    
    public static __initboat() {
        boat.x = 2
        boat.y = 4
    }
    
    public show_boat() {
        clear_led()
        led.plot(this.x, this.y)
    }
    
    public go_left() {
        if (this.x > 0) {
            this.x = this.x - 1
        }
        
    }
    
    public go_right() {
        if (this.x < 4) {
            this.x = this.x + 1
        }
        
    }
    
}

boat.__initboat()

let cnt = 0
let myBoat = new boat()
basic.forever(function on_forever() {
    
    myBoat.show_boat()
    if (input.buttonIsPressed(Button.B)) {
        cnt = cnt + 1
    } else if (input.buttonIsPressed(Button.A)) {
        cnt = cnt - 1
    } else {
        cnt = 0
    }
    
    if (cnt == 1) {
        myBoat.go_right()
    }
    
    if (cnt == -1) {
        myBoat.go_left()
    }
    
    basic.pause(10)
})
