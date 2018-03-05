x=int(input("enter the number"))
fact=1
if x<0:
    print("enter the correct input")
elif x==0:
    print("factorial is not exist")
else:
    for i in range(1,x+1):
    fact=fact*i
    print("factorial is",fact)
    
