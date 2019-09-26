def my_func(n):
    return lambda a:a*n


"""
this is (my_doubler) is now considred lambda
"""
my_doubler = my_func(2)
my_tripler = my_func(3)

"""
parsing (4) to lambda (my_doubler)
مرة نضاعف الرقم، مرة 3 أضعاف
"""

print(my_doubler(4))
print(my_tripler(4))
print("a")
