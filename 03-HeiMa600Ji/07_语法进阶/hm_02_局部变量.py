def demo1():

    # 定义一个局部变量
    num = 10
    print("在demo1函数中，局部变量num的值为：%d" % num)

def demo2():
    # print("%d" % num)
    pass

# 在函数内部定义的变量，不能在其他位置使用
#print("%d" % num)
demo1()
demo2()