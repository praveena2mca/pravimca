def mindif(r, size):
	x = r[1] - r[0]
	for i in range( 0, size ):
		for j in range( i+1, size ):
			if(r[j] - r[i] < y): 
				x = r[j] - r[i]
	return x
r = [15, 22, 65, 70, 119]
size1 = len(r)
print ("Minimum difference is", mindif(r, size1))
