let TEM_THRESHOLD = 40
let LIGHT_THRESHOLD = 200
radio.setGroup(5)
let tem_value = 0
let light_value = 0
function sample_data() {
    
    tem_value = tem_value + input.temperature()
    light_value = light_value + input.lightLevel()
}

//  0: sample data
//  1: handle data and send signal
let cur_st = 0
let cnt = 0
basic.forever(function on_forever() {
    let tem_avg: number;
    let light_avg: number;
    
    if (cur_st == 0) {
        sample_data()
        cnt = cnt + 1
        if (cnt == 10) {
            cnt = 0
            cur_st = 1
        }
        
    } else if (cur_st == 1) {
        tem_avg = tem_value / 10
        light_avg = light_value / 10
        if (tem_avg > TEM_THRESHOLD) {
            //  heat warning
            console.log(0)
            radio.sendNumber(0)
        } else {
            console.log(1)
            radio.sendNumber(1)
        }
        
        if (light_avg < LIGHT_THRESHOLD) {
            //  light warning
            console.log(3)
            radio.sendNumber(3)
        } else {
            console.log(2)
            radio.sendNumber(2)
        }
        
        cur_st = 0
        tem_value = 0
        light_value = 0
    }
    
    basic.pause(10)
})
