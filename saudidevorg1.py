list1 = [1,2,3,4]

newList = list1.copy()

print(newList)

list1.pop(0)

print(list1)
print(newList)

newList = list1

list1.pop(0)
print(list1)
print(newList)

list1.insert(0,1)
list1.insert(1,2)
print(list1)


newList = list(list1)
list1.pop(0)
print(newList)

newList = list((1,2,3,4,5))

print(newList)
