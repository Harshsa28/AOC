f = open("input.txt", "r");

data = []

for each in f:
	if each[-1] == '\n':
		data.append(each[:-1])
	else:
		data.append(each)

maxi = 0

ids = []

for i in data:
	row = i[:7]
	col = i[7:]
	assert(len(row)==7)
	try:
		assert(len(col)==3)
	except:
		print(len(col))
		print(col)
		exit()
	num = 0
	r = 0
	c = 0
	for j in range(len(row)):
		if row[j] == 'B':
			r += 2**(6-j)
	for j in range(len(col)):
		if col[j] == 'R':
			c += 2**(2-j)
	t = r*8+c
	maxi = max(maxi,t)
	ids.append(t)

print(ids)
		
for i in range(len(ids)):
	if (ids[i]-2 in ids and ids[i]-1 not in ids):
		print(ids[i]-1)
	elif (ids[i]+2 in ids and ids[i]+1 not in ids):
		print(ids[i]+1)
		
print(675 in ids)
print(674 in ids)
print(676 in ids)



