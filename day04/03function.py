def sum_2num(a,b):
	if not isinstance(a,(int,float)):
		print("传入的a是%s，不是一个数字类型"%a)
		return
	if not isinstance(b,(int,float)):
		print("传入的b是%s,不是一个数字类型"%b)
		return
	sum = a + b
	return sum
s = sum_2num(1,2)
print(s)
