class Person():
	def __init__(self,name,age,height):
		self.name = name
		self.age = age
		self.height = height
	def introduce(self):
		print("姓名：%s,年龄为：%s"%(self.name,self.age))

p1 = Person("zs",18,1.72)
p1.introduce()
