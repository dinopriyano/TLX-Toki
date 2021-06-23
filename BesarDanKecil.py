n = int(input())

for j in range(n):
    inp = input()
    result = ""
    idx = 1

    for i in inp:
        if idx%2 == 1:
            result += i.upper()
        else:
            result += i.lower()

        idx += 1

    print(result)