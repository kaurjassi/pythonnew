def reverse(l):
    reverse_list = [i[::-1] for i in l]
    return reverse_list

names = ['jaswinder' , 'mandeep' , 'kajal', 'tushar']
print(reverse(names))    