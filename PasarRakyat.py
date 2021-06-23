import math

n = int(input())
kpk = 1
for i in range(n):
    d = int(input())
    kpk = kpk * (d/math.gcd(int(kpk), d))

print(str(int(kpk)))