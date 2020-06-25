# guessing number game......
winning_number = 18
guess = 1
guessing_number = input("ENTER A NUMBER: ")
guessing_number = int(guessing_number)
game_over = False
while not game_over:
    if winning_number == guessing_number:
        print(f"YOU WIN!!!, you win in {guess} attempts. ") 
    elif guess == 9:
        print(f"sorry, you take {guess} attempts. play again...")   
        game_over = True
    else:
        if winning_number < guessing_number :
            print("NUMBER IS TOO HIGH")
            guess += 1
            guessing_number = int(input("ENTER A NUBMER AGAIN:"))
        elif winning_number > guessing_number :
            print("NUMBER IS TOO LOW")
            guess += 1
            guessing_number = int(input("ENTER A NUBMER AGAIN: "))
        
            
            
                        
                    
   
    
 

