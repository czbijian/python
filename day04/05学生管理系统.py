print("="*30)
print("学生管理系统".center(22))
print("输入1：表示添加学生")
print("输入2：查找学生")
print("输入3：修改学生")
print("输入4：删除学生")
print("输入5：查看所有学生")
print("输入6：退出")
stus = []
while True:
	operate = input("请输入你想要的操作：")
	if operate == "1":
		name = input("请输入学生的姓名：")
		age = input("请输入学生的年龄：")
		qq = input("请输入学生的qq：")
		stu = {}
		stu["name"]=name
		stu["age"]=age
		stu["qq"]=qq
		stus.append(stu)
		print("添加成功")
	if operate == "2":
		name = input("请输入要查找的学生的姓名：")
		for item in stus:
			if item["name"] == name.strip():
				print("%s学生存在，年龄为：%s,qq号为：%s",(item["name"],item["age"],item["qq"]))
				break
		else:
			print("学生%s没有找到"%name)
	if operate == "3":
		pass
	if operate == "4":
		pass
	if operate == "5":
		print("序号\t姓名\t年龄\tQQ号")
		for i,item in enumerate(stus,1):
			print("%s\t%s\t%s\t%s"%(i,item["name"],item["age"],item["qq"]))
	if operate == "6":
		break
