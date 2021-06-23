n,m = map(int, input().split())

for i in range(n):
    for j in range(m):
        if (i+1)%2 == 0 and (j+1)%2 == 0:
            print("#", end ="")
        elif (i+1)%2 == 1 and (j+1)%2 == 1:
            print("*", end ="")
        elif (i+1)%2 == 0 or (j+1)%2 == 0:
            print("$", end ="")

    print("")