x=int(input("enter x"))
y=int(input("enter y"))
l=[]
for i in range(x):
    a=int(input("enter x val"))
    l.append(a)
for j in range(y):
    c=0
    u=int(input())
    v=int(input())
    for i in range(u,v):
        c=c+int(l[i])
    print(c)
