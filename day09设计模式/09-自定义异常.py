class PasswordException(Exception):
	def __init__(self,pw,min_length):
		self.password = pw
		self.min_length = min_length
	def __str__(self):
		return "%s的密码错误，密码的最小长度为%s"%(self.password, self.min_length)

def reg(username, password):
	if len(password) < 6:
		raise PasswordException(password,6)
	else:
		print("用户名为：%s,密码为：%s"%(username,password))

try:
	reg("zs","124")
except Exception as ex:#两个except,会按照顺序先执行第一，如果第一个满足异常类型条件，进入第一excep，不会进入后面的excep。
	print("第一个except")
	print(ex)
except PasswordException as ex:
	print("第二个except")
	print(ex)
