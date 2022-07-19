class User(object):
	name = 'zs' #公共的类属性
	__password = "123456"#私有(隐藏)的类属性

	def __init__(self, sex, username):
		self.sex = sex
		self.username = username

u = User("男","james")
print(u.name)
u2 = User("","sdfs")
print(u2.name)
