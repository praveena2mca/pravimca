def hun(l):
	for i in range(len(l)):
		if i==l[i]:
			print(i)
	
def main():
	try:
		n=int(input())
		l=[]
		for i in range(n):
			l.append(int(input()))
		hun(l)
	except:
		print('invalid')
main()
