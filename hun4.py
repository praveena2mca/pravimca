def hun4(l,n):
	c=0
	for i in range(n):
		for j in range(n):
			if l[i]==l[j]:
				c=c+1
		if c==1:
			print(l[i])
		c=0
def main():
	n=int(input())
	l=[]
	for i in range(n):
		l.append(int(input()))
	hun4(l,n)
try:
	main()
except:
	print('invalid')
