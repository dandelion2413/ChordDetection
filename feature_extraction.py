import numpy
f1 = open('./testfile.txt', 'w+')
f2 = open('./feature_extraction.txt', 'w+')
f_y = open('../KEYS', 'r')

song_KEYS = [0 for i in xrange(180)]
song_names = [0 for i in xrange(180)]
count = int(0)
for line_KEYS in open('../KEYS', 'r'):
	tmpkey,tmpname  = line_KEYS.split()
	count = count + 1
	# print line_KEYS
print count

song_count = 0

for line_dir_name in open('./data_directory_name.txt', 'r'):
	# print line_dir_name[0:len(line_dir_name)-1]
# Array = [[0 for i in xrange(6)] for i in xrange(300)] 
	for line_lab in open(line_dir_name[0:len(line_dir_name)-1], 'r'):
		# for line in open('./A_Hard_Day_s_Night/01-A_Hard_Day_s_Night.lab', 'r'):
		# line_lab = line_lab.split()
		count = int(0)
		Chord_sum = float(0)
		data_Chord = [0 for i in xrange(300)] 
		# Chord = [[0 for i in xrange(12)] for i in xrange(2)]
		Chord = [0 for i in xrange(25)]
		Chord_kind = [0 for i in xrange(25)]
		# print line_lab[0:len(line_lab)-2]
		lab_filename = line_lab[0:len(line_lab)-1]+".lab"
		# print lab_filename
		Chord[0] = 1
		Chord_kind[0] = 1
		song_count = song_count + 1
		for line in open(lab_filename, 'r'):
		    tmpA, tmpB, data_Chord[count] = line.split()
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
		    	Chord_sum = Chord_sum + 1
		    count = count + 1
		ans = 0
		tmp = 0
		Chord = numpy.array(Chord)
		for i in xrange(0,25):
			if(i<1):
				print >>f2, "%lf " %(Chord[i]),
			elif(i<24):
				print >>f2, "%lf " %(Chord[i]/Chord_sum),
			else:
				print >>f2, "%lf" %(Chord[i]/Chord_sum)
		# print >>f2, Chord
print song_count
