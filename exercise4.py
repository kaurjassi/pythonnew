winning_number= 68
guessed_number=input("Enter A Random Number: ")
guessed_number=int(guessed_number)
if winning_number == guessed_number:
    print("YOU WIN!!!!!!!")
else:   
    if guessed_number < winning_number:
        print("Number Is Too Low ") 
    else:
        print("Number Is Too High")

    
    
