class A(object):
	def test(self):
		print("A-----test()")
class B(object):
	def test(self):
		print("B-----test()")

class C(B,A):
	def test1(self):
		print("C-----test1()")

c = C()
print(C.__mro__)#打印优先级
c.test()
