x=int(input("enter the number"))
reverse=0
while(x>0):
    s=x%10
    reverse=reverse*10+s
    x=x//10
print(reverse)
