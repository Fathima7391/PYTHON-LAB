d={}
n=int(input("enter the number of elements="))
for i in range(n):
    d[i]=input("enter the elements:")
a=sorted(d.values())
print("ascending:",a)
a.reverse()
print("desc",a)