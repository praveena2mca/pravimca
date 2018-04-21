def dairy():
	x=0
	l=[]
	n=int(input())
	for i in range(n):
		l.append(int(input()))
	for i in l:
		x+=(n-i)
	print(x)
  
try:
  dairy()
except:
  print('invalid')
  
