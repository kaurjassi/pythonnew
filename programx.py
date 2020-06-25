def word_counter(s):
    count = {}
    for char in s:
        count[char] = s.count(char)
    return count
    
        

name = "mandeep"
print(word_counter(name))
     