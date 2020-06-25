def even_odd(l):
    even = []
    odd = []
    total = []
    for i in l:
        if i % 2 == 0 :
            even.append(i)
        else:
            odd.append(i)
            total = [odd , even]
    return total    
numbers = [1,2,3,4,5,6,7,8,9,10]
print(even_odd(numbers))
