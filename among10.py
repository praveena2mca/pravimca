a=[]
n=int(input("enter the elements:"))
for i in range(1,n+1):
    b=int(input("enter the element:"))
    a.append(b)
a.sort()
print("the maximum number of element:",a[n-1])
