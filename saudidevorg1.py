thisSet = {1,'a',4,'python', 100}

print(thisSet)

for x in thisSet:
    print(x)

thisSet.update([123,212,'ABC'])

print(thisSet)

print(len(thisSet))

thisSet.remove(123)
thisSet.discard(212)

print(thisSet)

thisSet.pop()

print(thisSet)

thisSet.clear()

print(thisSet)
