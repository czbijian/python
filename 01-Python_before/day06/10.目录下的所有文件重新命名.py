import os
file_list = os.listdir("testdir/")
for f in file_list:
#	print(f)
	dest_file="re-"+f#重新命名之后的目标文件名
#	os.rename("testdir/"+f,"testdir/"+dest_file)
	#采用绝对路径的形式写代码
	parent_dir = os.path.abspath("testdir/")#动态获取父目录绝对路径
	#文件的绝对路径=父目录的绝对路径+/+文件名
	source_file = os.path.join(parent_dir,f)
	dest_file = os.path.join(parent_dir,dest_file)
	os.rename(source_file, dest_file)
