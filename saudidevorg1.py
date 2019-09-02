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

list = ["a", "b", "c", "d", 1, 2]
print(list[1:3])
list = ["Python"]* 5
print(list)
list = [3.4,2.12,5.7]
list = list+numbersList
print(list)
