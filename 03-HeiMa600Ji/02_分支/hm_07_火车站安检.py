# 1.定义布尔型变量has_ticket表示是否有车票
has_ticket = True

# 2.定义整型变量knife_length表示刀的长度，单位：厘米
knife_length = 10

# 3.首先检查是否有车票，如果有，才允许进行安检
if has_ticket:
    print("车票检查通过，准备开始安检")
    # 4.安检时，需要检查刀的长度，判断是否超过20厘米
    if knife_length > 20:
    # 如果超过20厘米，提示刀的长度，不充许上车
        print("您携带的刀太长了，有%d公分长"%knife_length)
        print("不允许上车")
    # 如果不超过20厘来，安检通过
    else:
        print("安检已经通过，祝您旅途愉快。")
# 5.如果没有车票，不充许进门
else:
    print("大哥，请先买票")