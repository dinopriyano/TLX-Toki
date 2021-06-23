n = int(input())
for i in range(n):
    n,a,b,k = map(int, input().split())
    sisa = n + ((b-a)*k)
    print(f"Kasus #{str(i+1)}: {str(sisa)}")
