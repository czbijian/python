num = 10
# 再定义一个全局变量
title = "Hello World"



# 再定义一个全局变量
name = "小明"

def demo():

    print("%s" % num)
    print("%s" % title)
    print("%s" % name)  # 这里会报错，因为name是局部变量，不能在函数外使用

demo()