str=input("enter the string=")
str=str.split()
str1=[]
for i in str:
    if i not in str1:
        str1.append(i)
print(str1)
for i in range (0,len(str1)):
    print( str.count(str1[i]))
