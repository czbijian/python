from sys import argv, path  # 导入特定的成员

print('================python from import===================================')
print('path:', path)  # 因为已经导入path成员，所以此处引用时不需要加sys.path
print('argv:', argv)  # 因为已经导入argv成员，所以此处引用时不需要加sys.argv