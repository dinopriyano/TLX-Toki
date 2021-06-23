n,m = map(int, input().split())
for i in range(n):
    if (i + 1) % 2 == 1:
        print("W"*m)
    elif (i + 1) % 2 == 0:
        print("B"*m)


