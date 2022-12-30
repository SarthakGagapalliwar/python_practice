#summary of all what i study tell

#1 string
name = "SaRthak"
#2 string indexing
print(name[-1])
#3 string slicing
print(name[0:2])
print(name[:-2])
#4 take user input
age = int(input("enter your age ;"))
print(age)
#5 take two user inputs
user_name, name = input("enter your name and age : ").split(",")
print(user_name)
print(age)
# #6 len function
print(len(name))
# #7 lower, upper, title method
print(name.lower())
print(name.upper())
print(name.title())
#8 find, replace, center method
print(name.find("a")) # for first a
a_pos=name.find("a")
a_pos2=name.find("a", a_pos +1)
print(a_pos2)
#**sarthak**
print(name.center(11, "*"))
# string are immutable
name="sarthak"
print(name.replace("a","A",1)) # 1= change one a only which come first
print(name) #then also string is not changing this is call immutable








