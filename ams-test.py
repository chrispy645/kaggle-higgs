import math
import sys
import numpy

f = open("out.test.csv")
f.readline()

arr_b = []
arr_s = []

arr_b_prob = []
arr_s_prob = []

x = 350000
for line in f:
	line = line.rstrip()
	if line == "":
		break
	
	line = line.split(',')
	
	inst = int(line[0])
	actual = line[1].split(':')[1]
	pred = line[2].split(':')[1]
	prob = float(line[4])
	
	entry = {'inst': x, 'pred': pred, 'rank': 0}
	
	if pred == 's':
		arr_s.append(entry)
		arr_s_prob.append(prob)
	else:
		arr_b.append(entry)
		arr_b_prob.append(prob)
		
	x += 1
	
f.close()

tt=set([x for x in range(1,550000+1)])

sortd = list(numpy.argsort(arr_b_prob))
c = 1
for idx in sortd:
	arr_b[idx]['rank'] = c
	tt.remove(c)
	c += 1
	
sortd = list(numpy.argsort(arr_s_prob))[::-1]
c=550000
for idx in sortd:
	arr_s[idx]['rank'] = c
	tt.remove(c)
	c -= 1
	
print "EventId,RankOrder,Class"
for each in arr_b:
	print ",".join( [ str(each['inst']), str(each['rank']), str(each['pred']) ] )
for each in arr_s:
	print ",".join( [ str(each['inst']), str(each['rank']), str(each['pred']) ] )
	

