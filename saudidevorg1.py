class Person:
    def __init__(self, fname, lname):
        self.firstname=fname
        self.lastname=lname

    def printname(self):
        print(self.firstname,self.lastname)



class Student(Person):
    def __init__(self, fname, lname, age):
        Person.__init__(self,fname,lname)
        self.age=age

    def printage():
        print(age)

y=Student("Sara", "Ahmad", 5)

y.printname()
print(y.age)
