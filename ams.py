import math

f = open("out.csv")
f.readline()

arr = []

for line in f:
	line = line.rstrip()
	if line == "":
		break
	
	line = line.split(',')
	
	actual = line[1].split(':')[1]
	pred = line[2].split(':')[1]
	
	entry = {'actual': actual, 'pred': pred, 'weight': 0}
	arr.append(entry)
	
f.close()

# --------

f = open("training.csv.fold3.arff")
while True:
	st = f.readline().rstrip()
	if st == "@data":
		break
		
for each in arr:
	line = f.readline().rstrip().split(',')
	each['weight'] = float(line[ len(line)-2 ])
f.close()

s=0.0
b=0.0

for i in range(0, len(arr)):
	wi = arr[i]['weight']
	yi = arr[i]['actual']
	yi_hat = arr[i]['pred']
	
	if yi == 's' and yi == yi_hat:
		s += wi
	
	if yi == 'b' and yi == yi_hat:
		b += wi
		
		
br=10.0
sbb = s+b+br

brk = math.log( 1+(s/(b+br)), 2 )

ams = math.sqrt( 2 * ( (sbb*brk)-s ) )

print ams

