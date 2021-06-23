text = input()

textArr = text.split(" ")
numOne = int(textArr[0])
numTwo = int(textArr[2])
operate = textArr[1]

if operate == "-":
    print(str(numOne - numTwo))
elif operate == "+":
    print(str(numOne + numTwo))
elif operate == "*":
    print(str(numOne * numTwo))
elif operate == "<":
    print("benar" if (numOne < numTwo) else "salah")
elif operate == ">":
    print("benar" if (numOne > numTwo) else "salah")
elif operate == "=":
    print("benar" if (numOne == numTwo) else "salah")
