def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
         return b
    else:
        return c
num1=int(input("enter your first number : "))
num2=int(input("enter your second number : "))
num3=int(input("enter your third number : "))
biggest=greatest(num1, num2, num3)
print(f"{biggest} is your greatest number")
    
    
