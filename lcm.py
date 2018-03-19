print("*****LCM****")
def lcm(x,y):
    if x>y:
        greater=x
    else:
        greater=y
    while(true):
        if((greater%x==0) and (greater%y==0)):
            lcm=greater
            break
        greater=greater+1
    return lcm
f1=int(input("enter the first value"))
f2=int(input("enter the second value"))
print("lcm of",f1 ",and",f2 ,"is",lcm(f1,f2))
