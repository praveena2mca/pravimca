def num(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            num = i
    return num
a =int(input("enter a number")) 
b= int(input("enter a number")) 
print(num(a,b))
