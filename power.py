def power(n):
    n = n/2
    if n == 2:
        print("Yes")
    elif n > 2:
        return power(n)
    else:
        print("no") 
s=int(input("enter a number:"))
print(power(s))
