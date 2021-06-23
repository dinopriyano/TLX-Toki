s = input()
x, y = 0, 0
for way in s:
    if way == "R":
        x += 1
    elif way == "L":
        x -= 1
    elif way == "U":
        y += 1
    elif way == "D":
        y -= 1

print(str(x) + " " + str(y))
