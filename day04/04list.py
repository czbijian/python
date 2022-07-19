names=['zs','ls','ww','sl']
names2=("zs","ls","ww","sl")
j = 0
#第一种迭代，显示序号
print("序号\t姓名")
for i in names:
	j+=1
	print("%d\t%s"%(j,i))
#第二种 枚举
for i,item in enumerate(names,1):
	print("%d\t%s"%(i,item))


