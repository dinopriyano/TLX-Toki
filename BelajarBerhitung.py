n = int(input())
numMin = 1000000000
numMax = 0
sum = 0

for i in range(n):
    inp = input().split(" ")
    l = int(inp[0])
    r = int(inp[1])

    numMin = min(numMin,min(l,r))
    numMax = max(numMax,max(l,r))

if numMin > 1:
    sum = int((numMax*(numMax+1))/2) - int(((numMin-1)*((numMin-1)+1))/2)
else:
    sum = int((numMax * (numMax + 1)) / 2)

print(str(sum))