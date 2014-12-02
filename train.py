import math
import numpy
def sign(w, x):
	if(numpy.dot(w, x) >= 0):
		return 1
	else:
		return -1
def theta(s):
	return (1+math.exp(-s))**(-1) 

X = [[[0 for i in xrange(25)] for i in xrange(50)] for i in xrange(24)]
X_c = [0 for x in xrange(24)]
X_t = [[0 for i in xrange(25)] for i in xrange(200)]
Y_t = [0 for i in xrange(200)]
# Y = [0 for i in xrange(200)]

c = 0

for line in open('../output/Reorder.txt', 'r'):
	t = line.split()
	idn = int(t[25])
	for i in xrange(25):
		if(i == 0):
			X[idn][X_c[idn]][i] = int(t[i])
			X_t[c][i] = int(t[i])
		else:
			X[idn][X_c[idn]][i] = float(t[i])
			X_t[c][i] = float(t[i])
	# Y[idn] = idn
	X[idn] = numpy.array(X[idn])
	X_t[i] =  numpy.array(X_t[i])
	Y_t[i] = int(t[25])
	X_c[idn] = X_c[idn] + 1
	c = c + 1
# print X[5]
w = [[[0 for i in xrange(25)] for i in xrange(24)] for i in xrange(24)]

for a in xrange(0,23):
	for b in xrange(a+1, 24):
		tmp_total = X_c[a] + X_c[b]
		if(tmp_total == 0):
			# print b, 0
			continue
		# tmpX = numpy.concatenate((X[a], X[b]), axis=0)
		tmpX = [[0 for i in xrange(25)] for i in xrange(tmp_total)] 
		tmpY = [0 for x in xrange(tmp_total)]
		for i in xrange(tmp_total):
			# tmpY[i] = 1 if(i<X_c[a]) else 0
			# tmpY[i] = -1 if(i<(X_c[b]+50) and i>50) else 0
			tmpY[i] = 1 if(i<X_c[a]) else -1
			tmpX[i] = X[a][i] if(i<X_c[a]) else X[b][i-X_c[a]]
		# print 'i=', i
		tmpX_plus = numpy.linalg.pinv(tmpX)

		w[a][b] = numpy.inner(tmpX_plus, tmpY)
			
		for i in range(100):
			grad_E = 0
			for j in range(tmp_total):
				# print -tmpY[j]*numpy.dot(w[0], tmpX[j]), -tmpY[j]*tmpX[j]
				grad_E = grad_E + theta(-tmpY[j]*numpy.dot(w[a][b], tmpX[j]))*(-tmpY[j]*tmpX[j])
			grad_E = grad_E / (tmp_total+1)
			w[a][b] = w[a][b] - 0.001 * grad_E
			# grad_E = 0
			# for j in range(c):
			# 	grad_E = grad_E + theta(-tmpY[j]*numpy.dot(w[a][b], tmpX[j]))*(-tmpY[j]*tmpX[j])
			# grad_E = grad_E / c
			# w[1] = w[1] - 0.01 * grad_E
			# grad_E = 0
			# mod_i = i % (tmp_total)
			# grad_E = grad_E + theta(-tmpY[mod_i]*numpy.dot(w[a][b], tmpX[mod_i]))*(-tmpY[mod_i]*tmpX[mod_i])
			# w[a][b] = w[a][b] - 0.001 * grad_E
		# Ein = 0
		# for i in xrange(tmp_total):
		# 	Ein = Ein + (sign(w[a][b],tmpX[i]) != tmpY[i])
		# print b, Ein / float(tmp_total)

Ein = 0
for t in xrange(180):
	# print X_t[t]
	vote = [0 for i in xrange(24)]
	for i in xrange(0,23):
		for j in xrange(i+1,24): 
			if(sign(w[i][j],X_t[t]) == 1):
				vote[i] = vote[i] + 1
			elif(sign(w[i][j],X_t[t]) == -1):
				vote[j] = vote[j] + 1
			else:
				continue
			# print i, j, w[i][j]
	maxVote = 0
	argMaxVote = 0
	# print vote
	for i in xrange(24):
		if(maxVote < vote[i]):
			maxVote = vote[i]
			argMaxVote = i
	Ein = Ein + (argMaxVote != Y_t[t])
	# if (argMaxVote >= 12):
	# 	argMaxVote = argMaxVote - 12
	# 	if(argMaxVote >= 8):
	# 		if((argMaxVote+2)%2):
	# 			print chr((argMaxVote+2)/2 + ord('a')), '#', argMaxVote+12
	# 		else:
	# 			print chr((argMaxVote+2)/2 + ord('a')), argMaxVote+12
	# 	elif(argMaxVote >= 3):
	# 		if((argMaxVote+1)%2):
	# 			print chr((argMaxVote+1)/2 + ord('a')), '#', argMaxVote+12
	# 		else:
	# 			print chr((argMaxVote+1)/2 + ord('a')), argMaxVote+12
	# 	else:
	# 		if((argMaxVote)%2):
	# 			print chr((argMaxVote)/2 + ord('a')), '#', argMaxVote+12
	# 		else:
	# 			print chr((argMaxVote)/2 + ord('a')), argMaxVote+12
	# else:
	# 	if(argMaxVote >= 8):
	# 		if((argMaxVote+2)%2):
	# 			print chr((argMaxVote+2)/2 + ord('A')), '#', argMaxVote
	# 		else:
	# 			print chr((argMaxVote+2)/2 + ord('A')), argMaxVote
	# 	elif(argMaxVote >= 3):
	# 		if((argMaxVote+1)%2):
	# 			print chr((argMaxVote+1)/2 + ord('A')), '#', argMaxVote
	# 		else:
	# 			print chr((argMaxVote+1)/2 + ord('A')), argMaxVote
	# 	else:
	# 		if((argMaxVote)%2):
	# 			print chr((argMaxVote)/2 + ord('A')), '#', argMaxVote
	# 		else:
	# 			print chr((argMaxVote)/2 + ord('A')), argMaxVote
	# print 'tune:', argMaxVote, maxVote
print Ein / float(c)

