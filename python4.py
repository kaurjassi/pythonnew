""" def my_map(func , l):
    new_list = []
    for item in l:
        new_list.append(func(item))
    return new_list
l = [1,3,4,5,6]    
print(my_map (lambda a : a**3 ,l))    """ """multi line comment"""



"""def outer_func():
    def inner_func():
        print("here is a message")
    return inner_func

jassi = outer_func()
jassi() 

 def new_func(a):
    def old_func(b):
        return a**b
    return old_func


man = new_func(3)
print(man(4)) """


import math
num = 25
num_sqrt = math.sqrt(num)
print(num_sqrt)



     
