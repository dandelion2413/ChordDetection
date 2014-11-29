import math
import numpy
# import random

# def sign(w, x):
# 	if(numpy.dot(w, x) > 0):
# 		return 1
# 	else:
# 		return -1

fAns = open('../output/lab_tuning_ans.txt', 'w+')

tune = [[0 for i in xrange(25)] for i in xrange(24)]


tune[0] = [ 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1 ,0 ,1 ,0 ,0 ,0 , 0, 1, 0, 0]
tune[12] = [ 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0 , 0, 0]

for i in xrange(1,12):
	for j in xrange(0,25):
		if(j==0):
			tune[i][j] = 1
		elif(j<13):
			tune[i][j] = tune[i-1][(j+12-2)%12+1]
		else:
			tune[i][j] = tune[i-1][(j+12-2)%12+13]
for i in xrange(13,24):
	for j in xrange(0,25):
		if(j==0):
			tune[i][j] = 1
		elif(j<13):
			tune[i][j] = tune[i-1][(j+12-2)%12+1]
		else:
			tune[i][j] = tune[i-1][(j+12-2)%12+13]

# print "   ",
# print [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5]
# for i in range(24):
# 	print "%2d " %(i),
# 	print tune[i]

Array = [[0 for i in xrange(6)] for i in xrange(300)] 
for lineLab in open('../beatles/lists/A_Hard_Day_s_Night.txt', 'r'):
	count = int(0)
	dataChord = [0 for i in xrange(300)] 
	Chord = [0 for i in xrange(25)]
	Chord_kind = [0 for i in xrange(25)]
	labFileName = '../beatles/chordlabs/' + lineLab[0:len(lineLab)-1] + '.lab'
	print labFileName
	for line in open(labFileName, 'r'):
	    tmpA, tmpB, dataChord[count] = line.split()
	    if(ord(dataChord[count][0])-ord('A') < 7):
	    	distance = ord(dataChord[count][0])-ord('A')
	    	if(dataChord[count].find('min') == -1):
	    		is_min = 0
	    	else:
	    		is_min = 1
	    	if(dataChord[count][0:5].find('#') != -1):
	    		accidental = 1
	    	elif(dataChord[count][0:5].find('b') != -1):
	    		accidental = -1
	    	else:
	    		accidental = 0
	    	if(distance > 4):
	    		Chord[(distance * 2 + 10 + accidental)%12 + is_min * 12 + 1] = Chord[(distance * 2 + 10 + accidental)%12 + is_min * 12 + 1] + 1
	    		Chord_kind[(distance * 2 + 10 + accidental)%12 + is_min * 12 + 1] = 1
	    	elif(distance > 1):
	    		Chord[(distance * 2 + 11 + accidental)%12 + is_min * 12 + 1] = Chord[(distance * 2 + 11 + accidental)%12 + is_min * 12 + 1] + 1
	    		Chord_kind[(distance * 2 + 11 + accidental)%12 + is_min * 12 + 1] = 1
	    	else:
	    		Chord[(distance * 2 + 12 + accidental)%12 + is_min * 12 + 1] = Chord[(distance * 2 + 12 + accidental)%12 + is_min * 12 + 1] + 1
	    		Chord_kind[(distance * 2 + 12 + accidental)%12 + is_min * 12 + 1] = 1
	    elif(ord(dataChord[count][0])-ord('a') < 7):
	    	distance = ord(dataChord[count][0])-ord('a')
	    	if(dataChord[count].find('min') == -1):
	    		is_min = 0
	    	else:
	    		is_min = 1
	    	if(dataChord[count][0:5].find('#') != -1):
	    		accidental = 1
	    	elif(dataChord[count][0:5].find('b') != -1):
	    		accidental = -1
	    	else:
	    		accidental = 0
	    	if(distance > 4):
	    		Chord[(distance * 2 + 10 + accidental)%12 + is_min * 12 + 1] = Chord[(distance * 2 + 10 + accidental)%12 + is_min * 12 + 1] + 1
	    		Chord_kind[(distance * 2 + 10 + accidental)%12 + is_min * 12 + 1] = 1
	    	elif(distance > 1):
	    		Chord[(distance * 2 + 11 + accidental)%12 + is_min * 12 + 1] = Chord[(distance * 2 + 11 + accidental)%12 + is_min * 12 + 1] + 1
	    		Chord_kind[(distance * 2 + 11 + accidental)%12 + is_min * 12 + 1] = 1
	    	else:
	    		Chord[(distance * 2 + 12 + accidental)%12 + is_min * 12 + 1] = Chord[(distance * 2 + 12 + accidental)%12 + is_min * 12 + 1] + 1
	    		Chord_kind[(distance * 2 + 12 + accidental)%12 + is_min * 12 + 1] = 1
	    count = count + 1
	ans = 0
	tmp = 0
	for x in range(24):
		if(numpy.dot(tune[x], Chord) + numpy.dot(tune[x], Chord_kind) > tmp):
			tmp = numpy.dot(tune[x], Chord) + numpy.dot(tune[x], Chord_kind)
			ans = x
	if(ans >= 8):
		print >>fAns, chr((ans+2)/2 + ord('A'))
	elif(distance >= 1):
		print >>fAns, chr((ans+1)/2 + ord('A'))
	else:
		print >>fAns, chr((ans)/2 + ord('A'))
	print Chord