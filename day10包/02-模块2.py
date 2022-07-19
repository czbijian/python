#使用自己制作的模块
#import module1
from module1 import isnull,test1
#from module1 import *  #python标准中不建议使用这种方式
#from module2 import *  #如果两个模块中方法名字相同，则后面覆盖前面
a = ''
#print(module1.isnull(a))
print(isnull(a))
test1()
