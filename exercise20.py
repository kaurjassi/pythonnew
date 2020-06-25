def multiply_list(num , *args):
    if args:
        return [i**num for i in args]
    else: 
        return "you didn't pass any args"  

 
print(multiply_list(4,*[3,4,5]))
