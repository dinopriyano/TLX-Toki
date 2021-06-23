inp = input().split(" ")
p = int(inp[0])
q = int(inp[1])

sum = (p**2) + (q**2) + 1
if sum % 4 == 0:
    print(str(int(sum/4)))
else:
    print(str(-1))