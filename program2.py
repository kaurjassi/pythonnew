name , char =input("enter your name and charchter : ").split(",")
print(f"length of your name is : {len(name.strip())}")
print(f"charchter count : {name.strip().lower().count(char.strip().lower())}")