import os
def read_stus():
	'''文件中存放数据的格式
	zs\t33\t2222333
	ls\t22\t2332323
	ww\t33\t3232323
	'''
	if os.path.exists(file_name):
		f = open(file_name,"r")
		while True:
			student_str = f.readline()
			if student_str=="":
				break
			else:
				student_info = student_str.split()
				student = {"name":student_info[0],"age":student_info[1],"qq":student_info[2]}
				stus.append(student)

def write_stus_to_fie():
	if os.path.exists(file_name):
		if os.path.exists(backup_file):
			os.remove(backup_file)
		os.rename(file_name,"backup-"+file_name)
	f = open(file_name,"w")
	for student in stus:
		student_str = "%s\t%s\t%s"%(student['name'],student['age'],student['qq'])
		f.write(student_str)
		f.write("\n")
	f.close()
def print_menu():
	print("="*30)
	print("学生管理系统".center(22))
	print("输入1：表示添加学生")
	print("输入2：查找学生")
	print("输入3：修改学生")
	print("输入4：删除学生")
	print("输入5：查看所有学生")
	print("输入6：退出")
def add_studetn():
	name = input("请输入学生的姓名：")
	age = input("请输入学生的年龄：")
	qq = input("请输入学生的qq：")
	stu = {}
	stu["name"]=name
	stu["age"]=age
	stu["qq"]=qq
	stus.append(stu)
	print("添加成功")
	
def search_student(name):
	for item in stus:
		if item["name"] == name.strip():
			print("%s学生存在"%name)
			print_student(item)
			return item
	else:
		print("学生%s没有找到"%name)
	
def print_student(item):
	print("%s\t%s\t%s"%(item["name"],item["age"],item["qq"]))
def print_all_students():
		print("序号\t姓名\t年龄\tQQ号")
		for i,item in enumerate(stus,1):
			print("%s\t"%i, end="")
			print_student(item)
def del_student(name):
	student = search_student(name)
	stus.remove(student)

def main():
	print_menu()
	read_stus()
	while True:
		operate = input("请输入你想要的操作：")
		if operate == "1":
			add_studetn()
			write_stus_to_fie()
		if operate == "2":
			name = input("请输入要查找的学生的姓名：")
			search_student(name)
		if operate == "3":
			pass
		if operate == "4":
			name = input("请输入要删除的学生姓名：")
			del_student(name)
			print("删除学生%s成功"%name)
			write_stud_to_file()
		if operate == "5":
			print_all_students()
		if operate == "6":
			break
file_name = "stus.txt"#存放学生数据的文件
backup_file = "backup-stus.txt"
#一个学生包含很多信息，一个学生一个字典。学生列表用列表存储
stus = []
main()
