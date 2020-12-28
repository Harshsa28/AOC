f = open("input.txt", "r");

data = []

for each in f:
	if each[-1] == '\n':
		data.append(each[:-1])
	else:
		data.append(each)

d = {} #dictionary

for i in data:
	r = i.split(' ')
	if (len(r) == 7):
		d[r[0]+' '+r[1]] = ""
	elif (len(r)-8)%4 == 0:
		d[r[0]+' '+r[1]] = []
		temp = 4
		while temp < len(r)-1:
			d[r[0]+' '+r[1]].append(r[temp]+' '+r[temp+1]+' '+r[temp+2])
			temp += 4 
	else:
		print("error in parsing data")
		print(r)
		print(len(r))
		exit()

print(d)
print('\n'*5)
n = {}

def memoization(i):
	print("in mem i is: ",i)
	if i in n:
		print("1 i is :", i)
		return n[i]
	elif d[i] == '':
		print("2 i is :", i)
		n[i] = 1
		return 1
	#	elif 'shiny gold' in d[i]:
	#		cont.add(i)
	#		return True
	else:
		n[i] = 1 
		for j in d[i]:
			temp = j.split(' ')
			n[i] += int(temp[0])*memoization(temp[1]+' '+temp[2])
		print("3 i is :", i)
		return n[i]

#for i in d:

memoization('shiny gold')

print(n)
print(n['shiny gold']-1)

