text = input()
halo = "halo dunia"
countRes = 0

for i in range(len(text)):
    if text[i].lower() == halo[i]:
        countRes += 1

print(str(countRes))