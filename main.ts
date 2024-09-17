let HEART_TIME = 2
// second
let TIMER = 0.1
//  0: intial state
//  1: show heart in first 2 seconds
//  2: show firework 
let cur_st = 0
let cnt = 0
let idx = 0
function display_fw(frame_num: number) {
    if (frame_num == 0) {
        basic.showLeds(`
        .....
        .....
        .....
        .....
        ..#..
        `, 1)
    } else if (frame_num == 1) {
        basic.showLeds(`
        .....
        .....
        .....
        ..#..
        .....
        `, 1)
    } else if (frame_num == 2) {
        basic.showLeds(`
        .....
        .....
        ..#..
        .....
        .....
        `, 1)
    } else if (frame_num == 3) {
        basic.showLeds(`
        .....
        ..#..
        .###.
        ..#..
        .....
        `, 1)
    } else if (frame_num == 4) {
        basic.showLeds(`
        .#.#.
        #.#.#
        .###.
        #.#.#
        .#.#.
        `, 1)
    } else if (frame_num == 5) {
        basic.showLeds(`
        .....
        .#.#.
        #.#.#
        .###.
        #####
        `, 1)
    } else if (frame_num == 6) {
        basic.showLeds(`
        .....
        .....
        .#.#.
        #.#.#
        #####
        `, 1)
    } else if (frame_num == 7) {
        basic.showLeds(`
        .....
        .....
        .....
        .#.#.
        #####
        `, 1)
    } else if (frame_num == 8) {
        basic.showLeds(`
        .....
        .....
        .....
        .....
        #####
        `, 1)
    }
    
}

basic.forever(function on_forever() {
    
    //  state machine
    if (cur_st == 0) {
        cnt = 0
        cur_st = 1
    } else if (cur_st == 1) {
        basic.showIcon(IconNames.Heart, 1)
        cnt = cnt + 1
        if (cnt == HEART_TIME * 100) {
            cnt = 0
            idx = 0
            cur_st = 2
        }
        
    } else if (cur_st == 2) {
        display_fw(idx)
        cnt = cnt + 1
        if (cnt == TIMER * 100) {
            cnt = 0
            idx = idx + 1
            if (idx == 9) {
                idx = 0
            }
            
        }
        
    }
    
    basic.pause(1)
})
