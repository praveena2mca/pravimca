x=str(input("enter the string:"))
x=x.casefold()
res=reversed(x)
if list(x)==list(res):
    print("yes")
else:
    print("no")
