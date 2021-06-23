a,b = map(int,input().split())
for i in range(10):
    bil = int((a + b) / 2)
    print(str(bil))
    what = input()
    if what == "terlalu kecil":
        a = bil + 1
    elif what == "terlalu besar":
        b = bil - 1
    elif what == "selamat":
        break