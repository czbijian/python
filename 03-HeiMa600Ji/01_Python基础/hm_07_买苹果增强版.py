# 1.输入苹果单价
price_str=input("请输入苹果价格：")
# 2.要求苹果重量
weight_str=input("请输入苹果重量：")
# 3.计算支付的总金额
# 注意：两个字符串变量之间是不能直接用惩罚的
# money = price * weight

# 1>将苹果单价转换成小数
price = float(price_str)
# 2>将苹果重量转换成小数
weight=float(weight_str)
# 3>计算付款金额
money = price * weight
print(money)