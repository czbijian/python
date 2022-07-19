class User(object):
	name = 'zs' #公共的类属性
	__password = "123456"#私有(隐藏)的类属性

	def __init__(self, sex, username):
		self.sex = sex
		self.username = username

class QQ_User(User):
	pass

u = User("男","james")	
print(QQ_User.name)#name是从父类继承过来的。name属于类属性，可以直接通过类来访问，也可以通过类的对象来访问
print(u.name)
#类属性修改,只能通过类来修改
User.name = 'ls'#真正的类属性修改
u.name = 'ww'#本质上没有修改类属性，仅仅给该对象定义了一个对象属性name，并且赋值为ww
print(u.name)
print(User.name)
#print(User.__password)
del u.name#本质上删除了对象的name属性，并没有删除类的属性
print(User.name)
