stu={"name":"laoxiao","age":"33"}

for k in stu.keys():
	print(k)
for v in stu.values():
	print(v)
print("="*30)
#迭代字典常用方式
for item in stu.items():
	print("key为：%s,value为：%s"%item)
print("="*30)
key = "name"
if key in stu:
	print("%s在字典中"%key)
