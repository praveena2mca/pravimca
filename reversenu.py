x=int(input("enter the number:"))
res=0
while(x>0):
    d=x%10
    res=res*10+d
    n=n//10
print("the reverse of number:",res)
