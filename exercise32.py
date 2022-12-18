# EXERCISE - WATCH COCO
# Ask user's name and age
# is user's name start with ("a" or ("A")) and age is above 10 then
# print "you can watch coco movie"
# Else print "sorry, you cannot watch coco"


# EXERCISE SOLUTION

winning_number=27
user_input =int(input("guess a number b/w 1 and 100 : "))
if user_input == winning_number:
    print("YOU WIN !!!!")
else: # nested if else
    if user_input < winning_number:
        print("too low")
    else:
        print("too high")    
        