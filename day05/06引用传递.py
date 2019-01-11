def test1(x,y):
	x.replace("c","C")#关键在这里，该结果x和a指向同一个地址。
#如果改为x=x.replace("c","C")，则x与a指向不同的地址
	y.append(10)
	print("x变量指向的内存地址为：%s"%id(x))
	print("y变量指向的内存地址为：%s"%id(y))

a = "abcdefg"
b = [1,2,3]
print("a变量指向的内存地址为：%s"%id(a))
print("b变量指向的内存地址为：%s"%id(b))
test1(a,b)

