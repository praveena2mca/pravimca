def sop(a,d,n):
    s=0
    i=0
    while i<n:
        s=s+a
        a=a+d
        i=i+1
    return s
n=20
a=2.5
d=1.5
print(sop(a,d,n))
