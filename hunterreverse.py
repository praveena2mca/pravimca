x=str(input())
a=x.split()
for i in range(len(a)):
    a[i] = a[i][::-1]
x=' '.join(a)
print(x)
