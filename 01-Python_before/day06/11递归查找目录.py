import os
#从/home/james/codes/python目录中找包含有hello的py文件是哪些
file_list = []
#递归函数，
def find_hello(parent_dir,file_name):
	file_abspath = os.path.join(parent_dir, file_name)
	if os.path.isdir(file_abspath):#判断当前文件是一个目录
		for f in os.listdir(file_abspath):#进入目录，列出目录下所有文件列表
			find_hello(file_abspath,f)#递归调用自己本身的函数
	else:#如果传入的文件是一个文件
		if file_abspath.endswith(".py"):#判断文件名是否以.py结尾
			if read_and_find_hello(file_abspath):#读取该py结尾的文件
				file_list.append(file_abspath)

def read_and_find_hello(py_file):
	flag = False
	f = open(py_file)
	while True:
		line = f.readline()
		if line == '':#文件读到最后一行，终止循环
			break
		elif "hello" in line:
			flag = True
			break
	f.close()
	return flag

find_hello("/home/james/codes","python")
print(file_list)
#print(read_and_find_hello("/home/james/codes/python/day06/06数值交换.py"))
