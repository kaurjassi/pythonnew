#name = input("enter your name:")
#print(name[::-1])
def is_palandrome(name):
    if name[::-1] == name :
        return True
    return False


name = input("Enter Your Name: ")
print(is_palandrome(name))
    
