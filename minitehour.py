a=int(input("enter the t1 hour"))
b=int(input("enter the t1 minites"))
c=int(input("enter the t2 hour"))
d=int(input("enter the t2 minites"))
e=a*60+b
f=c*60+d
g=e-f
print(g//60 'hr', g%60 'min')
