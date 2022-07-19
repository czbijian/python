class Animal:
	def __init__(self):
		print("动物的初始化")
		self.name = "动物"
	def eat(self):
		print("----吃饭----")
	def sleep(self):
		print("----睡觉----")

class Dog(Animal):
	def __init__(self, name):
		self.name = name
	def shout(self):
		print("----汪汪叫----")

class Cat(Animal):
#	def __init__(self):
#		print("猫初始化了")
	def catch(self):
		print("----抓老鼠----")

dog = Dog("小白")
dog.eat()
cat = Cat()
print(cat.name)
