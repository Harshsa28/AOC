f = open("input.txt", "r");

data = []

for each in f:
	if each[-1] == '\n':
		data.append(each[:-1])
	else:
		data.append(each)
		
c = 0
i = 0
while i < len(data):
	print(data[i])
	fire = []
	while (i != len(data) and data[i] != ""):
		ques = set()
		string  = data[i]
		for j in string:
			ques.add(j)
		fire.append(ques)
		i+=1
	assert(len(fire)>0)
	for j in range(len(fire)):
		fire[0] = fire[0].intersection(fire[j])
		#fire[j] = fire[j].intersection(fire[j+1])
	'''
	if len(fire)==1:
		print(fire[0])
		c += len(fire[0])
	else:
		print(fire[len(fire)-2])
		c += len(fire[len(fire)-2])
	'''
	print(fire[0])
	c += len(fire[0])
	i+=1
			
print(c)

