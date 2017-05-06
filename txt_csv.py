import csv

# count the length of generator
def count(iter):
    return sum(1 for _ in iter)

with open('cpu_info.txt', 'r') as in_file:
	stripped = (line.strip().split() for line in in_file)
	for i in range(10): # remove the first 10 lines in generator stripped
		next(stripped)

	# modify generator and simultaneously save in lst
	lst = []
	lst.append(next(stripped)) # save first PID line into lst
	num = count(lst[0]) # count how many features
	label = True # used to identify if line is gonna to save
	for i in stripped:
		if not i:
			continue
		if i[0] == 'Processes:':
			label = False
		if i[0] == 'PID':
			label = True
			continue # skip PID line
		if label == True:
			# modify 'command' feature format
			# i[1:3] means i[1] to i[2]
			if len(i) == num + 1:
				i[1:3] = [''.join(i[1:3])]
			elif len(i) == num + 2:
				i[1:4] = [''.join(i[1:4])]
			lst.append(i)

	with open('cpu_info.csv', 'w') as out_file:
		writer = csv.writer(out_file)
		writer.writerows(lst)