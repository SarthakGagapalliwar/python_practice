# replace() method
# find() method

string = "sujal is beautiful and he is good dancer"
print(string.replace(" ", "_" )) # in string all space is replace with(_)
print(string.replace("is", "was", 1)) # is replace with was 1=first is only
print(string.find("is")) # this the postion of first is
#for fiding second position of is
is_pos1=string.find("is")#is_pos1 ---> number
is_pos2=string.find("is", is_pos1 + 1) # +1 beause its count first is 
print(is_pos2)
#25