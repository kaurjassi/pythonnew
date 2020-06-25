import random 
winning_number = random.randint(1,100)
guess = 1
guessed_number = input("enter a random number b/w 1 and 100 : ")
guessed_number = int(guessed_number)
game_over = False
while not game_over :
    if winning_number == guessed_number : 
        print(f"you win , you guessed in {guess} attempts")
        game_over = True
    else :  
        if guessed_number < winning_number:
            print("TOO LOW")
            guess += 1
            guessed_number= int(input("guess again : "))
        else: 
            print("TOO HIGH")
            guess += 1
            guessed_number = int(input("guess again : "))

        