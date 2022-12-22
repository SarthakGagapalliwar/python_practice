# ask a number like 1453
#calculate sum of digit ---> 1+4+5+3

# logic , length = 4
# num = 1453
# int(num[0])-----> 1
# int(num[1])-----> 4
# int(num[2])-----> 5
# int(num[3])-----> 3
# i ----> 0 to 3

total=0
num=(input("Enter a number: "))
for i in range(0, len(num)):
    total += int(num[i])
    
print(total)    
