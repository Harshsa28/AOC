f = open("input.txt", "r");

data = []

for each in f:
	data.append(each)

slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]
ans = []
for [i,j] in slopes:
	x=0
	y=0
	trees = 0
	str_len = len(data[0])-1
	while(y<=len(data)-1):
		if x>=str_len:
			x-=str_len
		if (data[y][x] == '#'):
			trees+=1
		y+=j
		x+=i
	print(trees)
	ans.append(trees)

m = 1
for j in ans:
	m*=j
print(m)

