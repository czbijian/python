class User:
	def __init__(self, pw):
		if(len(pw)>=6):
			self.__password = pw
		else:
			print("密码：%s,密码不符合规定"%pw)
	def __str__(self):
		return "密码%s"%self.__password
	def get_password(self):
		return self.__password
u1 = User("123456")
#u1.__password = "123456"
#print(u1.__password)
print(u1.get_password())
print(u1)
