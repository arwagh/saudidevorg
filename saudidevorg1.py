thisTuple = (1,2,3,4)
print(thisTuple)
thisTuple = ()
print(thisTuple)
thisTuple = (3.1,4,5,"Python")
print(thisTuple)
print(thisTuple[0])

for x in thisTuple:
    print(x)

print(thisTuple[0:4])

print(3.1 in thisTuple)

thisTuple = (2,)*6
newTuple = (3,5,"a")
newestTuple = thisTuple + (4234,4234,21)
print(newestTuple)

print(len(thisTuple))

thisTuple = tuple((1,2,4,5))

print(thisTuple)

thisList = [1432,32,23]
print(tuple(thisList))
