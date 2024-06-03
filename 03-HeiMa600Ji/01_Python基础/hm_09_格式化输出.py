# 定义字符串变量name，输出 我的名字叫 小明， 请多多关照
name  = "大明"
print("我的名字叫%s,请多多关照！"%name)

# 定义整数变量 student_no, 输出 我的学号是 000001
student_no = 1
print("我的学号是 %06d"%student_no)

# 定义小数 price、weight、money
# 输出 苹果单价 9.00 元/斤，购买了 5.00斤，需要支付45.00元
price = 8.5
weight = 7.5
money = price * weight
print("苹果单价 %f 元/斤，购买了 %f斤，需要支付%f元"%(price, weight, money))

# 定义小数scale，输出数据比例是10.00%
scale = 0.25
print("数据比例是 %.2f %%" % (scale * 100))