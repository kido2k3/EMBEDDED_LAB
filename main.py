TEM_THRESHOLD = 40
LIGHT_THRESHOLD = 200
radio.set_group(5)
tem_value = 0
light_value = 0

def sample_data():
    global tem_value, light_value
    tem_value = tem_value + input.temperature()
    light_value = light_value + input.light_level()

# 0: sample data
# 1: handle data and send signal
cur_st = 0
cnt = 0
def on_forever():
    global cur_st, cnt, tem_value, light_value
    if cur_st == 0:
        sample_data()
        cnt = cnt + 1
        if cnt == 10:
            cnt = 0
            cur_st = 1
    elif cur_st == 1:
        tem_avg = tem_value / 10
        light_avg = light_value / 10
        if tem_avg > TEM_THRESHOLD:
            # heat warning
            print(0)
            radio.send_number(0)
        else:
            print(1)
            radio.send_number(1)
        if light_avg < LIGHT_THRESHOLD:
            # light warning
            print(3)
            radio.send_number(3)
        else:
            print(2)
            radio.send_number(2)
        cur_st = 0
        tem_value = 0
        light_value = 0
    basic.pause(10)
basic.forever(on_forever)