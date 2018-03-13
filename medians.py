def findMean(a,n):
    s=0
    for i in range(0,n):
        s+=a[i]
    return float(s/n)
def findMedian(a,n):
    sorted(a)
    if n%2!=0:
        return float(a[n/2])
    return float((a[int((n-1)(2)]+a[int(n/2)])/2.0)
a=[1,3,4,2,7,5,8,6]
n=len(a)
print("meadian'",findMean(a,n))
