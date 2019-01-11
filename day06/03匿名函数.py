def test(a,b,func):
	result = func(a,b)
	return result
print(test(2,3,lambda x,y:x*y))
