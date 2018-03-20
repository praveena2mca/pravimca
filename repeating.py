def PR(a,size):
    print("repeating element are",end='')
    for i in range(0,size):
        for j in range(i+1,size):
            if(a[i]==a[j]):
                print(a[i],end='')
a=[2,4,2,1,2,3,1]
a_size=len(a)
PR(a,a_size)
