k = int(input())

for i in range(1, k + 1, 1):
    for j in range(1, i + 1, 1):
        print("*", end='')
    print('')

for k in range(k, 0, -1):
    for l in range(k-1, 0, -1):
        print("*", end='')
    print('')
