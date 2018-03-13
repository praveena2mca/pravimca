x=int(input("enter the lower range:"))
y=int(input("enter the upper range:"))
for i in range(x,y+1):
    s=0
    temp=i
    while temp>0:
        d=temp%10
        s+=d**3
        temp//=10
    if i==s:
        print(i)
