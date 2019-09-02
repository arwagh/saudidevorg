numbersList = [1,2,3,4,5]
print(numbersList)
print(numbersList[0])
print(numbersList[1])
print(numbersList[-1])

numbersList[2] = 12
for x in numbersList:
    print(x)

del numbersList[0]
print(numbersList[0])
