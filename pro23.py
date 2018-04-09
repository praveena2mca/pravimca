N = 0
E = 1
S = 2
W = 3
def circle(h):
	a = 0
	b = 0
	dir = N
	for i in xrange(len(h)):
		move = h[i]
		if move == 'R':
			dir = (dir + 1)%4
		elif move == 'L':
			dir = (4 + dir - 1)%4

		else: 
			if dir == N:
				b += 1
			elif dir == E:
				a += 1
			elif dir == S:
				b -= 1
			else:
				a -= 1

	return (a == 0 and b == 0)

h =input("enter somthing in capitals")
if circle(h):
	print ("Given sequence of moves is circular:")
else:
	print ("Given sequence of moves is NOT circular:")
