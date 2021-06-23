bilangan = int(input())
fibonacci = [0, 1]
idx = 0
while True:
    if fibonacci[idx] == bilangan:
        print(str(idx+1))
        break
    elif fibonacci[idx] > bilangan:
        print("0")
        break

    fibonacci.append(fibonacci[idx] + fibonacci[idx+1])
    idx += 1