info_tuple = ("zhangsan", 18, 1.75, "zhangsan")

# 1.取值和取索引
print(info_tuple[0])
# 已经知道数据的内容，希望知道该数据在元祖中的索引
print(info_tuple.index("zhangsan"))

# 2.统计计数
print(info_tuple.count("zhangsan"))
print(len(info_tuple))
