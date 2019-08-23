import random
#This is comment
"""
This is multiple lines
of comments
"""
print("Hello World")
if 5 > 2:
    print("five is greater than two!")

w = "CS"
print(w)
w = 'CS'
print(w)

x = 5
y = "Arwa"
y = 8
print(x)
print(y)

a, b, c = "A", "B", "C"
print(a)
print(b)
print(c)

a = b = c = "Letter"
print(a)
print(b)
print(c)
print("It's a " + a)

a = "Python is"
b = "awesome"
print(a + b)

a = 5
b = 8
print(a+b)


x = 1
y = 2.8
z = 1j

print(type(x))
print(type(y))
print(type(z))

x = 432432432
y = 425
z = -32134124

print(type(x))
print(type(y))
print(type(z))


x = 1.434
y = 3.42342
z = -1.0e4

print(type(x))
print(type(y))
print(type(z))

x = 3+5j
y = -4j
z = 2j

print(type(x))
print(type(y))
print(type(z))

x = 3+5j
y = 4
z = 2.0

a = float(y)
b = int(z)
c = complex(y)

print(type(a))
print(type(b))
print(type(c))

print(random.randrange(1,10))
