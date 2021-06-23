allowCoin = [1000,500,200,100,50,20,10,5,2,1]
k = int(input())

idx = 0
while k > 0:
    bagi = int(k/allowCoin[idx])
    if bagi >= 1:
        print(str(allowCoin[idx])+" "+str(bagi))
        k -= (bagi * allowCoin[idx])

    idx += 1