a = 22 
b = 33
#借用元组
a,b = b,a
#借用中间变量
c = 0
c = a
a = b 
b = c
