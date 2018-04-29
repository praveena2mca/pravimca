 def p17():
	x=int(input())
	l=[]
	f=0
	for i in range(x):
		l.append(int(input()))
	k=int(input())
	for i in range(x-1):
		if l[i]==l[i+1]:
			s=l[i]+l[i+1]
			if s==k:
				f=1
				print('yes')
	if f!=1:
		print('no')
    
p17()
