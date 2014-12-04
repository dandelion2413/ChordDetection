import math
import numpy
# import random

# def sign(w, x):
# 	if(numpy.dot(w, x) > 0):
# 		return 1
# 	else:
# 		return -1

fAns = open('../output/lab_tuning_ans.txt', 'w+')
fReorderData = open('../output/Reorder.txt', 'w+')

tune = [[0 for i in xrange(25)] for i in xrange(24)]


# tune[0] = [ 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1 ,0 ,1 ,0 ,0 ,0 , 0, 1, 0, 0]
# tune[12] = [ 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0 , 0, 0]

# for i in xrange(1,12):
# 	for j in xrange(0,25):
# 		if(j==0):
# 			tune[i][j] = 1
# 		elif(j<13):
# 			tune[i][j] = tune[i-1][(j+12-2)%12+1]
# 		else:
# 			tune[i][j] = tune[i-1][(j+12-2)%12+13]
# for i in xrange(13,24):
# 	for j in xrange(0,25):
# 		if(j==0):
# 			tune[i][j] = 1
# 		elif(j<13):
# 			tune[i][j] = tune[i-1][(j+12-2)%12+1]
# 		else:
# 			tune[i][j] = tune[i-1][(j+12-2)%12+13]

# print "   ",
# print [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5]
# for i in range(24):
# 	print "%2d " %(i),
# 	print tune[i]


# dataTune = [[[0 for i in xrange(2)] for i in xrange(50)] for i in xrange(24)]
# dataTuneCount = [0 for i in xrange(24)]
dataTuneTotal = int(0)
tmpY = [[0 for i in xrange(2)] for i in xrange(250)]  
for line in open('../beatles/KEYS', 'r'):
 	tmpA, tmpB = line.split()
 	# print tmpA, tmpB
	accidental = 1 if(tmpA.find('#') != -1) else 0
	accidental = -1 if(tmpA.find('b') != -1) else accidental
 	if (ord(tmpA[0])-ord('A') < 7 and ord(tmpA[0])-ord('A') > -1):
 		distance = ord(tmpA[0])-ord('A')
	   	minorTune = 0
	elif(ord(tmpA[0])-ord('a') < 7 and ord(tmpA[0])-ord('a') > -1) :
		distance = ord(tmpA[0])-ord('a')
	   	minorTune = 1
	else:
		continue
	if(distance > 4):
		index = (distance * 2 + 10 + accidental)%12 + minorTune * 12  
	elif(distance > 1):
		index = (distance * 2 + 11 + accidental)%12 + minorTune * 12
	else:
		index = (distance * 2 + 12 + accidental)%12 + minorTune * 12
	
    
	# dataTune[index][dataTuneCount[index]][0] = tmpA
	# dataTune[index][dataTuneCount[index]][1] = tmpB
	# print dataTune[index][dataTuneCount[index]][0], dataTune[index][dataTuneCount[index]][1]
	# dataTuneCount[index] = dataTuneCount[index] + 1
	# tmpY[dataTuneTotal][0] = tmpA
	tmpY[dataTuneTotal][0] = index
	tmpY[dataTuneTotal][1] = tmpA
	dataTuneTotal = dataTuneTotal + 1
# print dataTune
# print dataTuneCount
# print tmpY
tmpYCount = int(0)
for album in open('../beatles/lists/lists.txt', 'r'):
	albumCat = '../beatles/lists/' + album[0:len(album)-1] + '.txt'
	for lineLab in open(albumCat, 'r'):
		dataChordCount = int(0)
		dataChord = [0 for i in xrange(300)] 
		Chord = [0 for i in xrange(25)]
		Chord_kind = [0 for i in xrange(25)]
		Chord[0] = 1
		Chord_kind[0] = 1
		labFileName = '../beatles/chordlabs/' + lineLab[0:len(lineLab)-1] + '.lab'
		# print labFileName
		for line in open(labFileName, 'r'):
		    tmpA, tmpB, dataChord[dataChordCount] = line.split()
		    is_min =  0 if(dataChord[dataChordCount].find('min') == -1) else 1
		    accidental = 1 if(dataChord[dataChordCount][0:5].find('#') != -1) else 0
		    accidental = -1 if(dataChord[dataChordCount][0:5].find('b') != -1) else accidental
		    if(ord(dataChord[dataChordCount][0])-ord('A') < 7):
		    	distance = ord(dataChord[dataChordCount][0])-ord('A')
		    	if(distance > 4):
		    		Chord[(distance * 2 + 10 + accidental)%12 + is_min * 12 + 1] = Chord[(distance * 2 + 10 + accidental)%12 + is_min * 12 + 1] + 1
		    		Chord_kind[(distance * 2 + 10 + accidental)%12 + is_min * 12 + 1] = 1
		    	elif(distance > 1):
		    		Chord[(distance * 2 + 11 + accidental)%12 + is_min * 12 + 1] = Chord[(distance * 2 + 11 + accidental)%12 + is_min * 12 + 1] + 1
		    		Chord_kind[(distance * 2 + 11 + accidental)%12 + is_min * 12 + 1] = 1
		    	else:
		    		Chord[(distance * 2 + 12 + accidental)%12 + is_min * 12 + 1] = Chord[(distance * 2 + 12 + accidental)%12 + is_min * 12 + 1] + 1
		    		Chord_kind[(distance * 2 + 12 + accidental)%12 + is_min * 12 + 1] = 1
		    	dataChordCount = dataChordCount + 1
		    elif(ord(dataChord[dataChordCount][0])-ord('a') < 7):
		    	distance = ord(dataChord[dataChordCount][0])-ord('a')
		    	if(distance > 4):
		    		Chord[(distance * 2 + 10 + accidental)%12 + is_min * 12 + 1] = Chord[(distance * 2 + 10 + accidental)%12 + is_min * 12 + 1] + 1
		    		Chord_kind[(distance * 2 + 10 + accidental)%12 + is_min * 12 + 1] = 1
		    	elif(distance > 1):
		    		Chord[(distance * 2 + 11 + accidental)%12 + is_min * 12 + 1] = Chord[(distance * 2 + 11 + accidental)%12 + is_min * 12 + 1] + 1
		    		Chord_kind[(distance * 2 + 11 + accidental)%12 + is_min * 12 + 1] = 1
		    	else:
		    		Chord[(distance * 2 + 12 + accidental)%12 + is_min * 12 + 1] = Chord[(distance * 2 + 12 + accidental)%12 + is_min * 12 + 1] + 1
		    		Chord_kind[(distance * 2 + 12 + accidental)%12 + is_min * 12 + 1] = 1
		    	dataChordCount = dataChordCount + 1
		# for x in range(24):
		# 	if(numpy.dot(tune[x], Chord) + numpy.dot(tune[x], Chord_kind) > tmp):
		# 		tmp = numpy.dot(tune[x], Chord) + numpy.dot(tune[x], Chord_kind)
		# 		ans = x
		# if(ans >= 8):
		# 	print >>fAns, chr((ans+2)/2 + ord('A'))
		# elif(distance >= 1):
		# 	print >>fAns, chr((ans+1)/2 + ord('A'))
		# else:
		# 	print >>fAns, chr((ans)/2 + ord('A'))
		Chord = numpy.array(Chord) / float(dataChordCount)
		for x in xrange(25):
			if (x == 0):
				print >>fReorderData, 1,
			else:
				print >>fReorderData, Chord[x],
		print >>fReorderData, tmpY[tmpYCount][0]
		print >>fAns, '%2d' %(tmpY[tmpYCount][0])
		tmpYCount = tmpYCount + 1
print tmpYCount, dataTuneTotal