f = open("input.txt", "r");

data = []

for each in f:
	data.append(each)

correct = 0

for i in range(len(data)):
	pw = data[i]
	[rule, word]= pw.split(':')
	[num, char] = rule.split(' ')
	[l,u] = num.split('-')
	l = int(l)
	u = int(u)
	if (word[l] == char and word[u] != char) or (word[l] != char and word[u] ==char):
		correct+=1

print(correct)


