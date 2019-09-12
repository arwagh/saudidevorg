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
print(len(list))
list.append("A-Z")
list.insert(0, "Hello World")
print(list[0])

print(list)

list.remove(3.4)
print(list)

list.pop()
print(list)
list.pop(3)
print(list)

#list.clear()
print(list)
#list = numbersList

#list = numbersList.copy()

list1 = list(numbersList)
print(list1)
