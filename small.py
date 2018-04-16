x=int(input("enter a"))
y=int(input("enter n"))
b=str(x)
l=[]
for i in range(len(b)):
    l.append(b[i])
for i in range(y,len(b)):
        print(int(l[i]),end=' ')
