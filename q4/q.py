f = open("input.txt", "r");

data = []

for each in f:
	data.append(each)

v = 0

i = 0

while i <= len(data)-1:
	req = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
	num = 0
	while (i <= len(data)-1 and data[i]!="" and data[i][:-1]!=""):
		ind = data[i].split(' ')
		for j in ind:
			[f,val] = j.split(':')
			if val[-1] == '\n':
				val = val[:-1]
			print("f is :",f,": and val is :", val, " and len of f is :", len(f))
			if f in req:
				if f == "byr":
					if len(val)==4 and int(val)>=1920 and int(val)<=2002:
						print("byr pass")
						num+=1
				elif f == "iyr":
					if len(val)==4 and int(val)>=2010 and int(val)<=2020:
						print("iyr pass")
						num+=1
				elif f == "eyr":
					if len(val)==4 and int(val)>=2020 and int(val)<=2030:
						print("eyr pass")
						num+=1
					else:
						print("eyr fail f is :",f," and int(val) is :", int(val))
				elif f == "hgt":
					if len(val)>=3:
						unit = val[-2:]
						if unit=="cm" or unit=="in":
							if unit=="cm":
								if int(val[:-2])>=150 and int(val[:-2])<=193:
									print("hgt pass")
									num+=1
							elif unit=="in":
								if int(val[:-2])>=59 and int(val[:-2])<=76:
									print("hgt pass")
									num+=1
				elif f == "hcl":
					if val[0]=='#':
						temp = val[1:]
						fail = False
						for k in temp:
							if k not in "0123456789abcdef":
								fail = True
								break
						if fail == False:
							print("hcl pass")
							num+=1
				elif f == "ecl":
					if val in ["amb","blu","brn","gry","grn","hzl","oth"]:
						print("ecl pass")
						num+=1
				elif f == "pid":
					if len(val) == 9:
						fail = False
						for k in val:
							if k not in "0123456789":
								fail = True
								break
						if fail == False:
							print("pid pass")
							num+=1

		if num == 7:
			v+=1
			break
		i+=1
	i+=1
	

print(v)



