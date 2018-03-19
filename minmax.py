a=[]
x=int(input("enter the number:"))
for i in range(1,x+1):
    b=input("enter element:")
    a.append(b)
    a.sort()
print(max(a))
print(min(a))
