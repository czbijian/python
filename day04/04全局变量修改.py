names = ["laowang","lisi","zhangsan"]
student = {"name":"laowang"}
a = "laogao"
b = 100
def test1():
	print("原始的全局变量为：%s"%names)
	names[1] = "laoxiao"
	student["age"] = 23
	global a
	a = "golbin"
	global b
	b = b+1
test1()
print("最后的全局变量为：%s"%names)
print("最后的全局变量为Student：%s"%student)
print("最后的全局变量a的值为：%s"%a)
