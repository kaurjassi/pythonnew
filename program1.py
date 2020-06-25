def greatest(a,b,c): 
    if c < a > b :
        return a 
    elif a < b > c  :
        return b
    else:
        return c


num1 = int(input("enter first number : "))  
num2 = int(input("enter second number : "))      
num3 = int(input("enter third number : "))
biggest = greatest (num1,num2,num3)
print(f"{biggest} is biggest")