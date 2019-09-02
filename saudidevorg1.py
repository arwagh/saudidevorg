x = 5
if (x > 5 or x == 5):
    print("True 1")

if (x > 5 and not(x == 5)):
    print("True 2")

x = ["a", "b"]
y = ["a","b"]
z = x

print(x is y)
print(x is z)

print("a" in z)
print("c" in x)
