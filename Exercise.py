#exercise 1

# ask user to 3 numbers and have to print average of three numbers using string formatting.

#bonu:- try to make all comma separated input in one line


#sir answer
# num1 = input("enter first number :")
# num2 = input("enter second number :")
# num3 = input("enter third number :")
# (int(num1) + int(num2) + int(num3)) / 3
# num1, num2, num3, = input("enter three number commma separated: ").split(",") # then we have to write input 3,3,3 @ then no need of all first three step
# print(f"avrage of three number : {(int(num1) + int(num2) + int(num3)) / 3}")

#my answer
num1 = int(input("enter first number :"))
num2 = int(input("enter second number :"))
num3 = int(input("enter third number :"))
print("avrage of three number",(num1+num2+num3) / 3)