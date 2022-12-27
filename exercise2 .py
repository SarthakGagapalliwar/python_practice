# define is_palindrom function that take one word in string as input
# and return true if it is palindrome else return false


#plindrome - word that reads same backward as forwards

#example
# is_palindrone("madam") -----> true
# is_palindrone("namea") -----> true
# is_palindrone("hourse") -----> false

# logic (algorithm)
#step 1 -> reverse the string
#step 2 -> compare reversed string with orginal string


# def is_palindrom(word):
#     reversed_word = word[-1::-1]
#     if word == reversed_word:
#         return True
#     else:
#         return False
# a=(input("Enter the name: "))

# print(is_palindrom(a))    


#2 for short
# def is_palindrom(word):
#     if word == word[-1::-1]:
#         return True
#     return False
# a=input("Enter a name : ")
# print(is_palindrom(a))



#3 for short
def is_palindrom(word):
    return word == word[-1::-1]
a=input("Enter a name : ")
print(is_palindrom(a))

