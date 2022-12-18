# if elif else statement
# show ticket prise
# 0 to 4 (free)
# 5 to 10 (150)
# 11 to 60 (250)
# above 60 (200)

age = int(input("please input your age : "))

if age==0 or age<0:
    print("you can't watch movie")
elif 0<age<=4:
    print("ticket prise : free")
elif 5<age<=10:
    print("ticket prise :150")
elif 10<age<=60:
    print("ticket prise :250")
else: 
    print("ticket prise :200")          