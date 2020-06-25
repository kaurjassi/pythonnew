def word_list(l):
    reverse = []
    for i in l:
      reverse.append(i[::-1])
    return reverse    


my_list = ['abc','uvw','xyz','qrs']
print(word_list(my_list))