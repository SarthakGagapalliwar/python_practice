#if statement

name= "sarthak"
if name == "Sarthak" or "sarthak":
   print("you are sarthak")
elif name == "mohit" or "Mohit":
    print("you are mohit")
else:
    print("you are not sarthak or mohit")
    
       
# while
i = 0
while i<10:
    print(i)
    i+=1    
 
    
#for loop  
for i in range(1,11,2):
    print(i) 
 
    
#break keyword   
for i in range(1,11):
    if i==5:
        break
    print(i) 

    
#continue keyword   
for i in range (1,11):
    if i==5:
        continue
    print(i)
         