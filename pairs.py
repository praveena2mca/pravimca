def pairs():
	f=1
	x=int(input())
	for i in range(1,x):
		f=f*i
	print(f)
try:
	pairs()
except:
	print('invalid')
  
