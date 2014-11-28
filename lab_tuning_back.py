import math
import numpy
# import random

# def sign(w, x):
# 	if(numpy.dot(w, x) > 0):
# 		return 1
# 	else:
# 		return -1



tune = [[0 for i in xrange(25)] for i in xrange(12)]
tune[0] = [ 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1 ,0 ,1 ,0 ,0 ,0 , 0, 1, 0, 0]

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
	    	if(data_Chord[count].find('#') != -1):
	    		accidental = 1
	    	elif(data_Chord[count].find('b') != -1):
	    		accidental = -1
	    	else:
	    		accidental = 0
	    	# if(count == 1):
	    	# 	print data_Chord[count].find('min')
	    	# 	print 'jizz'
	    	if(distance > 4):
	    		# Chord[is_min][distance * 2 - 2] = Chord[is_min][distance * 2 - 2] + 1
	    		Chord[(distance * 2 + 12 + accidental)%12 - 2 + is_min * 12 + 1] = Chord[(distance * 2 + 12 + accidental)%12 - 2 + is_min * 12 + 1] + 1
	    		Chord_kind[(distance * 2 + 12 + accidental)%12 - 2 + is_min * 12 + 1] = 1
	    	elif(distance > 1):
	    		# Chord[is_min][distance * 2 - 1] = Chord[is_min][distance * 2 - 1] + 1
	    		Chord[(distance * 2 + 12 + accidental)%12 - 1 + is_min * 12 + 1] = Chord[(distance * 2 + 12 + accidental)%12 - 1 + is_min * 12 + 1] + 1
	    		Chord_kind[(distance * 2 + 12 + accidental)%12 - 1 + is_min * 12 + 1] = 1
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

# print 'maj'
# print Chord[0:11]
# for x in range(12):
# 	# print Chord[0][x]
# 	print Chord[x]
# print 'min'
# print Chord[12:23]
# for x in xrange(12,24):
# 	# print Chord[1][x]
# 	print Chord[x]

# test_Matrix = [[0 for i in xrange(6)] for i in xrange(500)] 
# test_Array = [[0 for i in xrange(6)] for i in xrange(500)] 

# count = int(0)
# for line in open('hw1_18_test.dat', 'r'):
#     test_Matrix[count][1],test_Matrix[count][2],test_Matrix[count][3],test_Matrix[count][4],test_Matrix[count][5] = line.split()
#     test_Matrix[count][0],test_Matrix[count][1],test_Matrix[count][2],test_Matrix[count][3],test_Matrix[count][4],test_Matrix[count][5] = int(1),float(test_Matrix[count][1]),float(test_Matrix[count][2]),float(test_Matrix[count][3]),float(test_Matrix[count][4]),int(test_Matrix[count][5])
#     test_Array[count] = numpy.array([test_Matrix[count][0], test_Matrix[count][1], test_Matrix[count][2], test_Matrix[count][3], test_Matrix[count][4]])
#     count = count + 1



# e_Average = 0

# for x in range(2000):
# 	w = numpy.array([0, 0, 0, 0, 0])
# 	tmp_w = w
# 	flag = 1
# 	c = 0
# 	now_e = count
# 	tmp_e = 0
# 	error = 0
# 	while flag == 1:
# 		flag = 0
# 		rand_num = random.sample(xrange(0,500), 500)
# 		for i in range(count):
# 			if(sign(tmp_w, Array[rand_num[i]]) != Matrix[rand_num[i]][5]):
# 				tmp_w = tmp_w + Array[rand_num[i]] * Matrix[rand_num[i]][5]
# 				flag = 1
# 				c = c + 1
# 				for j in range(count):
# 					if(sign(tmp_w, Array[j]) != Matrix[j][5]):
# 						tmp_e = tmp_e + 1
# 						# print "%d" %(tmp_e)
# 				if(now_e > tmp_e):
# 					now_e = tmp_e
# 					w = tmp_w
# 				tmp_e = 0
# 			if c>99:
# 				break
# 		if c>99:
# 			break
# 	for y in range(count):
# 		if(sign(w, test_Array[y]) != test_Matrix[y][5]):
# 			error = error + 1
# 	e_Average = e_Average + error / float(count)

# print "%lf" %(e_Average / 2000)
# 		