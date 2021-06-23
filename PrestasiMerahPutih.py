n = int(input())
a = map(int, input().split())
x = int(input())
pos = 1

for i in a:
    if x == i:
        print(str(pos))
        break

    pos += 1
