import math
import numpy

count = int(0)
transTune = [[0 for i in xrange(2)] for i in xrange(250)]
for line in open('../beatles/KEYS', 'r'):
	transTune[count][0], transTune[count][1] = line.split()
	print transTune[count][0],transTune[count][1]
	if(ord(transTune[count][0])-ord('A') < 7):
	   	distance = ord(transTune[count][0])-ord('A')
	   	minorTune = 1
	   	if(transTune[count].find('min') == -1):
	   		is_min = 0
	   	else:
	   		is_min = 1
	   	if(transTune[count][0:5].find('#') != -1):
	   		accidental = 1
	   	elif(transTune[count][0:5].find('b') != -1):
	   		accidental = -1
	   	else:
	    	accidental = 0
	else:
		distance = ord(transTune[count][0])-ord('a')
		minorTune = -1
	   	if(transTune[count].find('min') == -1):
	   		is_min = 0
	   	else:
	   		is_min = 1
	   	if(transTune[count][0:5].find('#') != -1):
	   		accidental = 1
	   	elif(transTune[count][0:5].find('b') != -1):
	   		accidental = -1
	   	else:
	    	accidental = 0
	count = count + 1
print count