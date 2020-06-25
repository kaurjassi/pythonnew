age = int(input("ENTER YOUR AGE : \n"))
if len(str(age)) == 2:
    if age < 18:
        print("you are not eligible for license. \n")
    elif age > 18:
        print("you are eligible for license. \n")
    elif age == 18:
        print("we can not decided. \n")
else:
    print("ENTER A VALID AGE!!!!! \n")
   
    
    