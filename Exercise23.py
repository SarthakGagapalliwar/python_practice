#exercise
# take come separated input from user
# 1.) user's name
# 2.) a single character

#otput- 2 print lines 
# 1.) user's name length
# 2.) count the character thet user input (bonus case insensitive count)
#ans sArthak
name, char = input("enter comma separatd name and character :").split(",")
print("length of you name", len(name))
# name.lower()
# char.lower()
# print("charcter count : ", name.lower().count(char.lower()))
print("charcter count : ", name.strip().lower().count(char.strip().lower())) #  use this beacuse when we use 6 line code we cant give space on output writing in 7 code we can give space on writeing output

# print(name[1]) #first task
# print(len(name))
# print(name.count("a"))
