# ask user name and count each charcter
#"sarthak gagapalliwar"
# s=1
# a=6
# r=2
# t=1
# h=1 ....

name=input("Enter you name: ")
temp=""
for i in range (len(name)):
    if name[i] not in temp:
        print(name[i], name.count(name[i]))
        temp += name[i] # for cheaking dont repet leater again 