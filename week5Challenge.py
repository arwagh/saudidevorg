oddList = []
evenList = []
for x in range(3, 19 ,2):
    oddList.append(x)

for x in range(2,18,2):
    evenList.append(x)


for x in oddList:
    for y in evenList:
        print(x,y)
