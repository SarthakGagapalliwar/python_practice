# MODIFY NUMBER GUSSING GAME



winning_number = 46
guess = 1

number = int(input("guess a number between 1 to 100 : "))
game_over = False
while not game_over:
    if number == winning_number:
        print(f"you win, and you guesses this number in {guess} times ")
        game_over = True
    else:
        if number < winning_number:
            print("too low ")    
            guess += 1
            number =int(input("guess again : "))
        else:
            print("too high")
            guess += 1    
            number = int(input("guess again : "))