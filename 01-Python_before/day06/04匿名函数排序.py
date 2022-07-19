stus=[{"name":"zs","age":22},{"name":"laowang","age":33}]
#a = [22,2,3,27,34,1,78]
#a.sort(reverse = True)
#a.reverse()
#print(a)

stus.sort(key=lambda x:x["name"])#按名字排序
print(stus)
