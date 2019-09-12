thisList = [1,2,3,4]
thisList.append(5)

newList = thisList.copy()
print(newList)

print(thisList.count(1))

newList.insert(0,'a')
print(newList)

tuple = ("java", "python", "swift")
print("python" in tuple)
