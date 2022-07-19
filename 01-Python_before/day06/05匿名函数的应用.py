#encoding=UTF-8
def test(a,b,func):
	result = func(a,b)
	return result
#func_new = input("请输入你的操作:")
func_new = input("请输入你的操作：")
func_new = eval(func_new)#把字符串转换成可以执行的表达式
print(test(22,33,func_new))
