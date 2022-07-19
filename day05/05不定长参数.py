def test1(x,y,*args,z=10):
	print(x,y)
	print(args)#args的结果是一个元组（3,4,5,6,7)
	sum = x + y + z
	for i in args:
		sum += i
	print("和为%s"%sum)
def test2(x,*args,**kwargs):
	print(x)
	print(args)
	print(kwargs)
	sum = x
	for i in args:
		sum += i
	for i in kwargs.values():
		sum += i
	print("和为：%s"%sum)
test1(1,2,3,4,5,6,7,z=20)
print("="*30)
test2(2,3,4,num1=5,num2=6)
