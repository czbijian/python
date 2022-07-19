def get_num(n):
	if n == 1 or n == 2:
		return 1
	return get_num(n - 1) + get_num(n - 2)
#把获取的斐波那契数字存放到列表中
nums = []
for i in range(1,21):
	nums.append(get_num(i))#get_num获得一个斐波那契数字
print(nums)
