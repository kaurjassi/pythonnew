def reversed_list(l):
    reverse = []
    for i in range(len(l)):
        popped_item = l.pop()
        reverse.append(popped_item)
    return reverse     

number = [2,3,4,5]
print(reversed_list(number)) 