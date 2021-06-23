inp = input().split(" ")
a = int(inp[0])
x = int(inp[1])

mod = x % a
resi = int((x - mod) / a)
print(str(resi)+" "+str(mod))

