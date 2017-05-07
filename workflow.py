import subprocess
import csv

# collecting data time
sec = 5

"""Step 1: Take data into data.txt"""
proc = subprocess.Popen(['sh', 'makeData.sh'], stdout=subprocess.PIPE) 
print('Taking data into data.txt: PROCESSING...')
try:
	proc.wait(timeout=sec) # after time sec, the program runs proc.terminate
except subprocess.TimeoutExpired:
	proc.terminate()
print('Taking data into data.txt: DONE!!!')


"""Step 2: Convert data.txt to data.csv"""
print('Converting data.txt to data.csv: PROCESSING...')
# count the length of generator
def count(iter):
    return sum(1 for _ in iter)

with open('data.txt', 'r') as in_file:
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

	with open('data.csv', 'w') as out_file:
		writer = csv.writer(out_file)
		writer.writerows(lst)
print('Converting data.txt to data.csv: DONE!!!')


"""Step 3: Analyze data"""
print('Analyzing data: PROCESSING...')
proc = subprocess.Popen(['python', 'analysis.py'], stdout=subprocess.PIPE, shell=True)
print('Analyzing data: DONE!!!')
proc.terminate()