def HCF(x,y):
    if(x>y):
        smaller=y
    else:
        smaller=x
    for i in range(1,smaller+1):
        if((x%i==0) and (y%i==0)):
            hcf=i
        return hcf
 x1=int(input("enter the number"))
 x2=int(input("enter the number"))
 print("hcf is",x1,"and",x2,"is",HCF(x1,x2))
