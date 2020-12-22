f = open("input.txt", "r");

data = []

for each in f:
	data.append(int(each))

data.sort()

for i in range(len(data)):
	c = data[i]
	start = min(len(data)-1,i+1)
	end = max(0, len(data)-1)
	
	while (c != 2020 and start!=end):
		try:
			c = data[i]+data[start]+data[end]
		except:
			print("start is :", start,"and end is :", end)
			break
		if c < 2020:
			start+=1;
		elif c > 2020:
			end-=1;
		elif c==2020:
			print(data[i]*data[start]*data[end])
			break




		
