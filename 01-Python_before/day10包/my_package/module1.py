__all__ = ['isnull']#指定哪些函数可以被调用,python3之后很少使用了
#写一个工具方法，判断字符是否为null。当字符串为None，为null，还有‘’还为null，还有‘   ’也为null
def isnull(str):
	if not str:
		return True
	elif str.strip()=='':
		return True
	else:
		return False

def test1():
	print("------module1 中的test1方法")

if __name__=='__main__':#由python解释器主动执行该模块代码为了测试
#这行代码是测试代码。单独执行模块时执行。但是只要模板被导入，就会停止执行。
	print("是否为空%s"%isnull(""))
