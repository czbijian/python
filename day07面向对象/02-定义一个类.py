#定义了一个类
class Car:
	
	def start(self):#self不用传参
		print("汽车启动")
	def print_car_infor(self):
		print("车的名字是：%s,颜色为：%s"%(self.name,self.color))
c = Car()#构建一个对象
c.name = "迈腾"
c.color = "金色"
c.print_car_infor()
#c2 = Car()#再构建一个对象
c.start()
