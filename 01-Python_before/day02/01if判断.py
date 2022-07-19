age=int(input("请输入年龄:"))
sex=input("输入性别：")

#and 表示并且，or表示或者。not表示不满足后面的条件
if age >= 18 and sex == "男":
	print("可以做苦力了")
elif age< 18 or sex == "女":
	print("不用做苦力")
elif not (sex == '女' or sex == '男'):#sex != 女 and sex != 男
	print("人妖")
else:
	pass#以后要填充代码，为了保证不会出现语法错误
