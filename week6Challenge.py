#Question 1: write a recursion to calculate 5^3

def my_func(n, a):
    if(a>0):
        result = n * my_func(n,a-1)
        print("result: {}".format(result))
    else:
        result = 1
    return result

my_func(5,3)


#Quesion 2: write a list that contains: -4, -6, -5, -1, 2, 3, 7, 9, 88.
#Then write a lambda that prints only positive numbers

num_list = [-4,-6,-5,-1,2,3,7,9,88]

positive_list = list(filter(lambda x: (x>0), num_list))

print(positive_list)
