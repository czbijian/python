f = open('test1.txt','r')
str = f.read(3)
print("读取的数据是：%s"%str)
#查找当前的位置
position = f.tell()
print("当前文件位置：%s"%position)
str = f.read(3)
print("读取的数据是：%s"%str)
#查找当前的位置
position = f.tell()
print("当前文件位置：%s"%position)
