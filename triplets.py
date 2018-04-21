x=int(input("Enter upper limit:"))
y=0
m=2
while(y<x):
    for n in range(1,m+1):
        a=m*m-n*n
        b=2*m*n
        y=m*m+n*n
        if(y>x):
            break
        if(a==0 or b==0 or y==0):
            break
        print(a,b,y)
    m=m+1
