x=list(input())
y=list(input())
a=len(x)
b=len(y)
i=0
j=0
c=[]
while a>0:
    if x[i]==y[j]:
        c.append(x[i])
    j=j+1
    i=i+1
    a=a-1
print(b-len(c))
