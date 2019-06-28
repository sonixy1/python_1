List = []
Sub = []
Sub_Sub = []

for i in range(2, 10, 1):
    Sub_Sub.append("%d단 " % i)
    for j in range(1, 10, 1):
        Sub_Sub.append("%d * %d = %02d " % (i, j, i*j))
    Sub.append(Sub_Sub)
    Sub_Sub = []
    List.append(Sub)
    Sub = []

print(List)

for i in range(0, 8, 1):
    for j in range(0, 10, 1):
        print(List[i][0][j], end = '')
    print()
