from sys import maxint
def max(a,size):
	j = -maxint - 1
	s = 0
	for i in range(0, size):
		s = s + a[i]
		if (j < s):
			j = s
		if s < 0:
			s = 0
	return j
a = [-18, -23, -5, -2, -23, -12, -2, -1, -54, -2, -1, -45, -17]
print "Maximum contiguous sum is", max(a,len(a))
