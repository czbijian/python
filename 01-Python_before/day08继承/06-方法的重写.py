class Animal:
	#父类定义init方法
	def __init__(self):
		print("动物的初始化")
		self.color = "黄色"
	def eat(self):
		print("----吃饭----")
	def sleep(self):
		print("----睡觉----")

class Dog(Animal):
	#init和父类的init名字一样，所以叫方法的重写
	def __init__(self, name):
		super().__init__()#主动调用父类的init方法
		self.name = name
	def eat(self):
		super().eat()#调用父类的eat方法
		print("狗自己的eat方法")
	def shout(self):
		print("----汪汪叫----")

class Cat(Animal):
	#重写父类的init方法
	def __init__(self):
		print("猫初始化了")
	def catch(self):
		print("----抓老鼠----")
class ZangAo(Dog):
	def fight(self):
		print("----战斗----")

dog = Dog("小白")#如果子类中对某个方法重写了，优先调用自己本身的方法
#虽然init方法重写了，可是还想自动调用父类的init方法
print(dog.name)
print(dog.color)
dog.eat()
