name , char = input("enter your name and characters : ").split(",")
print(f"length of your name is{len(name)}")
print(f"character count :{name.lower().count(char.lower())}")

