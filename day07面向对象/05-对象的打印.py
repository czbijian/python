class Person():
	def __init__(self,name,age,height):
		self.name = name
		self.age = age
		self.height = height
	def __str__(self):
		return "姓名：%s,年龄为：%s,身高为:%s"%(self.name,self.age,self.height)
	def introduce(self):
		print("姓名：%s,年龄为：%s"%(self.name,self.age))

p1 = Person("zs",18,1.72)
print(p1)
