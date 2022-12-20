# ask a user for name
# Example - harshit varhisth
# print count of each words
# output :
        # h:1
        # a:2
        # r:3
        # s:3
        # h:3
        # ......
        
        
# ans>>>>       

name = input("please enter your name ")
# harshit vashisth
#harshit , len = 7-1 = 6
# name.count("h") , name.count(name[0]) =2
# name.count("a") , name.count(name[1]) =1
# name.count("r") , name.count(name[2]) =1
# name.count("s") , name.count(name[3]) =1
# name.count("h") , name.count(name[4]) =2
# name.count("i") , name.count(name[5]) =1

# output
# name[0] = h:2
#a : 1
#r : 1
#s : 1
#h : 2
temp_var = ""
i = 0
while i < len(name):
    if name[i] not in temp_var:
        temp_var += name[i]
        print(f"{name[i]} : {name.count(name[i])}")
    i += 1    
                