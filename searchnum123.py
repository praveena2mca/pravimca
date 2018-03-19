l=[11,65,2,3,1,2,4,5]
r=int(input("enter the number search"))
found=False
for i in range(len(i)):
    if(l[i]==r):
        found=True
        print("%d found is %dth position is ",(r,i))
        break
if(found==False):
    print("%d is not in lis %r")
