function display_lArrow(framenum: any) {
    if (framenum == 0) {
        basic.showLeds(`
            .....
            .....
            ....#
            .....
            .....
            `, 1)
    } else if (framenum == 1) {
        basic.showLeds(`
            .....
            ....#
            ...##
            ....#
            .....
            `, 1)
    } else if (framenum == 2) {
        basic.showLeds(`
            ....#
            ...#.
            ..###
            ...#.
            ....#
            `, 1)
    } else if (framenum == 3) {
        basic.showLeds(`
            ...#.
            ..#..
            .####
            ..#..
            ...#.
            `, 1)
    } else if (framenum == 4) {
        basic.showLeds(`
            ..#..
            .#...
            #####
            .#...
            ..#..
            `, 1)
    } else if (framenum == 5) {
        basic.showLeds(`
            .#...
            #....
            ####.
            #....
            .#...
            `, 1)
    } else if (framenum == 6) {
        basic.showLeds(`
            #....
            .....
            ###..
            .....
            #....
            `, 1)
    } else if (framenum == 7) {
        basic.showLeds(`
            .....
            .....
            ##...
            .....
            .....
            `, 1)
    } else if (framenum == 8) {
        basic.showLeds(`
            .....
            .....
            #....
            .....
            .....
            `, 1)
    }
    
}

function display_rArrow(framenum2: any) {
    if (framenum2 == 0) {
        basic.showLeds(`
            .....
            .....
            #....
            .....
            .....
            `, 1)
    } else if (framenum2 == 1) {
        basic.showLeds(`
            .....
            #....
            ##...
            #....
            .....
            `, 1)
    } else if (framenum2 == 2) {
        basic.showLeds(`
            #....
            .#...
            ###..
            .#...
            #....
            `, 1)
    } else if (framenum2 == 3) {
        basic.showLeds(`
            .#...
            ..#..
            ####.
            ..#..
            .#...
            `, 1)
    } else if (framenum2 == 4) {
        basic.showLeds(`
            ..#..
            ...#.
            #####
            ...#.
            ..#..
            `, 1)
    } else if (framenum2 == 5) {
        basic.showLeds(`
            ...#.
            ....#
            .####
            ....#
            ...#.
            `, 1)
    } else if (framenum2 == 6) {
        basic.showLeds(`
            ....#
            .....
            ..###
            .....
            ....#
            `, 1)
    } else if (framenum2 == 7) {
        basic.showLeds(`
            .....
            .....
            ...##
            .....
            .....
            `, 1)
    } else if (framenum2 == 8) {
        basic.showLeds(`
            .....
            .....
            ....#
            .....
            .....
            `, 1)
    }
    
}

//  0: left arrow
//  1: right arrow
let cur_st = 0
let idx = 0
let cnt = 0
basic.forever(function on_forever() {
    
    if (cur_st == 0) {
        display_lArrow(idx)
        if (input.buttonIsPressed(Button.B)) {
            cur_st = 1
            idx = 0
        }
        
    } else if (cur_st == 1) {
        display_rArrow(idx)
        if (input.buttonIsPressed(Button.A)) {
            cur_st = 0
            idx = 0
        }
        
    }
    
    cnt = cnt + 1
    if (cnt == 10) {
        cnt = 0
        idx = idx + 1
        if (idx == 9) {
            idx = 0
        }
        
    }
    
    basic.pause(10)
})
