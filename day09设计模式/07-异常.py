try:
	#a = 1
	print(a)
	i = 1/0
	print("hello")
except (NameError,ZeroDivisionError) as ex:#ex代表刚刚捕获的异常对象
	print("出现异常了")#捕获到异常之后不会回头继续执行之前的代码
	print(ex)
