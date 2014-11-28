import math
import numpy

tune = [[0 for i in xrange(25)] for i in xrange(12)]
tune[0] = [1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1 ,0 ,1 ,0 ,0 ,0 , 0, 1, 0, 0]

for i in xrange(1,12):
	for j in range(24):
		if(j==0):
			tune[i][j] = 1
		elif(j<13):
			tune[i][j] = tune[i-1][(j+12-2)%12+1]
		else:
			tune[i][j] = tune[i-1][(j+12-2)%12+12+1]

# for i in range(12):
# 	print tune[i]

f1 = open('./file.txt', 'w+')

# Array = [[0 for i in xrange(6)] for i in xrange(300)] 
for line_lab in open('../lists/A_Hard_Day_s_Night_lab.txt', 'r'):
	# for line in open('./A_Hard_Day_s_Night/01-A_Hard_Day_s_Night.lab', 'r'):
	# line_lab = line_lab.split()
	count = int(0)
	data_Chord = [0 for i in xrange(300)] 
	# Chord = [[0 for i in xrange(12)] for i in xrange(2)]
	Chord = [0 for i in xrange(25)]
	Chord_kind = [0 for i in xrange(25)]
	print line_lab[0:len(line_lab)-2]
	Chord[0] = 1
	Chord_kind[0] = 1
	for line in open(line_lab[0:len(line_lab)-2], 'r'):
	    tmpA, tmpB, data_Chord[count] = line.split()
	    # print data_Chord[count]
	    # sprint data_Chord[count][0]
	    distance = ord(data_Chord[count][0])-ord('A')
	    if(distance < 7):
	    	if(data_Chord[count].find('min') == -1):
	    		is_min = 0
	    	else:
	    		is_min = 1
	    	if(data_Chord[count][0:5].find('#') != -1):
	    		accidental = 1
	    	elif(data_Chord[count][0:5].find('b') != -1):
	    		accidental = -1
	    	else:
	    		accidental = 0
	    	# if(count == 1):
	    	# 	print data_Chord[count].find('min')
	    	# 	print 'jizz'
	    	if(distance > 4):
	    		# Chord[is_min][distance * 2 - 2] = Chord[is_min][distance * 2 - 2] + 1
	    		Chord[(distance * 2 + 10 + accidental)%12 + is_min * 12 + 1] = Chord[(distance * 2 + 10 + accidental)%12 + is_min * 12 + 1] + 1
	    		Chord_kind[(distance * 2 + 10 + accidental)%12 + is_min * 12 + 1] = 1
	    	elif(distance > 1):
	    		# Chord[is_min][distance * 2 - 1] = Chord[is_min][distance * 2 - 1] + 1
	    		Chord[(distance * 2 + 11 + accidental)%12 + is_min * 12 + 1] = Chord[(distance * 2 + 11 + accidental)%12 + is_min * 12 + 1] + 1
	    		Chord_kind[(distance * 2 + 11 + accidental)%12 + is_min * 12] = 1
	    	else:
	    		# Chord[is_min][distance * 2] = Chord[is_min][distance * 2] + 1
	    		Chord[(distance * 2 + 12 + accidental)%12 + is_min * 12 + 1] = Chord[(distance * 2 + 12 + accidental)%12 + is_min * 12 + 1] + 1
	    		Chord_kind[(distance * 2 + 12 + accidental)%12 + is_min * 12 + 1] = 1

	    # data_Chord[count][0]
	    # tmpA, tmpB, Chord[count] = float(tmpA),float(tmpB),
	    # Array[count] = numpy.array([Matrix[count][0], Matrix[count][1], Matrix[count][2], Matrix[count][3], Matrix[count][4]])
	    count = count + 1
	ans = 0
	tmp = 0
	for x in range(12):
		if(numpy.dot(tune[x], Chord) + numpy.dot(tune[x], Chord_kind) > tmp):
			tmp = numpy.dot(tune[x], Chord) + numpy.dot(tune[x], Chord_kind)
			ans = x
		# print (numpy.dot(tune[x], Chord) + numpy.dot(tune[x], Chord_kind))
	if(ans >= 8):
		print chr((ans+2)/2 + ord('A'))
	elif(distance >= 1):
		print chr((ans+1)/2 + ord('A'))
	else:
		print chr((ans)/2 + ord('A'))
	print >>f1, Chord