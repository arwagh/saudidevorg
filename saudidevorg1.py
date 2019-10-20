class MyNumbers:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        if self.a<=20:
            x=self.a
            self.a+=15
            return x
        else:
            raise StopIteration



myClass = MyNumbers();
myIter=iter(myClass)

print(next(myIter))
print(next(myIter))

my_tuple = ("apple","banana","cherry")
myit = iter(my_tuple)

#print(next(myit))
#print(next(myit))

#mystr = "banana"
#myit = iter(mystr)

#print(next(myit))
#print(next(myit))

#for x in my_tuple:
#    print(x)

#for x in mystr:
#    print(x)
