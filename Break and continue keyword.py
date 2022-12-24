
#break
# 1 to 11 print 
for i in range (1, 12):
    if i == 5:
        break
    print(i)
    
# continue    
# print 1 to 11 , but not 5
for i in range (1, 12):
    if i == 5:
        continue
    print(i)