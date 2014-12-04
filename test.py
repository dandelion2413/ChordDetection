import math
import numpy
def sign(w, x):
	if(numpy.dot(w, x) >= 0):
		return 1
	else:
		return -1
def theta(s):
	return (1+math.exp(-s))**(-1) 

X_t = [[0 for i in xrange(25)] for i in xrange(200)]
Y_t = [0 for i in xrange(200)]
# Y = [0 for i in xrange(200)]

c = 0

ftAns = open('../output/tAns.txt', 'w+')

for line in open('../output/Reorder.txt', 'r'):
	t = line.split()
	idn = int(t[25])
	# print idn
	for i in xrange(25):
		if(i == 0):
			X_t[c][i] = int(t[i])
		else:
			X_t[c][i] = float(t[i])
	# Y[idn] = idn
	X_t[c] =  numpy.array(X_t[c])
	Y_t[c] = idn
	c = c + 1
# print Y_t
# print X[5]

tmpW = [[0 for i in xrange(25)] for i in xrange(300)]
w = [[[0 for i in xrange(25)] for i in xrange(24)] for i in xrange(24)]


tmpWC = 0
for line in open('../output/W.txt', 'r'):
	t = line.split()
	for j in xrange(25):
		tmpW[tmpWC][j] = float(t[j])
	tmpWC = tmpWC + 1
print tmpWC
tmpWC = 0
for a in xrange(0,23):
	for b in xrange(a+1, 24):
		w[a][b] = tmpW[tmpWC]
		tmpWC = tmpWC + 1
			
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
	# print vote
	maxVote = 0
	argMaxVote = 0
	for i in xrange(24):
		if(maxVote < vote[i]):
			maxVote = vote[i]
			argMaxVote = i
	print >>ftAns, '%2d' %(argMaxVote)
	Ein = Ein + (argMaxVote != Y_t[t])

print Ein / float(c)

