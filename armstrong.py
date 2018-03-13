x=int(input("enter the number:"))
s=0
temp=x
while temp>0:
    d=temp%10
    s+=d**3
    temp//=10
if x==s:
    print(num,"is an armstrong number")
else:
    print(num,"it is not an armstrong number")
