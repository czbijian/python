row = 1

while row <= 5:
    col = 1
    while col <= row:
        print("*", end="")
        col += 1
    # print("第 %d 行"%row)
    # 这行代码的目的，就是在一行星星输出完成之后，添加换行！
    print()
    row += 1