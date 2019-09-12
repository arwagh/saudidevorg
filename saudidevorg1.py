thisDict = {1:"a",
            2:"b"}
print(thisDict)
print(thisDict[1])
print(thisDict.get(1))

thisDict[1] = 'c'

print(thisDict)


for x in thisDict:
    print(x)

for x in thisDict:
    print(thisDict[x])

for x in thisDict.values():
    print(x)

for x, y in thisDict.items():
    print(x, y)
