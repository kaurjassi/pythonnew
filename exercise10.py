def greater_num(a,b):
    if a>b :
        return a
    return b

num1 = int(input("enter first number : "))
num2 = int(input("enter second number : "))
bigger = greater_num(num1,num2)
print(f"{bigger} is greater")
