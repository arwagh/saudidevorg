i = 5
j = 4
while(i < 9):
    i+=1
    if(i==7):
        continue
    print(i)
else:
    print("finished looping")

thisList = ["a","b","c","d"]
print(type(thisList))
thisTuple = ("a",1,2,3)
print(type(thisTuple))
thisSet = {1,2,4,4}
print(type(thisSet))
thisDictionary = {1:"a",}
print(type(thisDictionary))

for x in thisSet:
    print(x)

for x in "python":
    if (x=="h"):
        continue
    print(x)
