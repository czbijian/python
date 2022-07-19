a = "123"
try:
	f = open("text.txt")
	try:
		content = f.read()
		content.index("hadoop")
	except ValueError as ex:#捕获所有异常
		print(ex)
	finally:
		print("最里面一层的finally")
except FileNotFoundError as ex:
	print(ex)
else:#没有异常的情况会自动执行的代码
	print("没有异常")
finally:#最终要执行的代码，不管前面是否出现exception
	print("finally")
	f.close()
