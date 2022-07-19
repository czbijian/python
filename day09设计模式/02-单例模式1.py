class User(object):
	__instance = None
	def __init__(self, name):
		self.name = name
	@classmethod
	def get_Instance(cls, name):
		if not cls.__instance:
			cls.__instance = User(name)
		return cls.__instance
#u1 = User("zs")
#u2 = User("ls")
u1 = User.get_Instance("zs")
u2 = User.get_Instance("ls")
print(u1.name)
print(u2.name)
print(u1 == u2)#==判断表达式如果返回True，这两个对象是一个对象，并且内存地址相同
print("u1对象的内存地址：%s,u2对象的内存地址：%s"%(id(u1),id(u2)))
