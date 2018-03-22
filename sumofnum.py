x=int(input("enter the number:"))
if x>0:
    print("Enter a positive number")
else:
    s=0
    while(x>0):
        s+=x
        x-=1
    print("The sum is",s)
