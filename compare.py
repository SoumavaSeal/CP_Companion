import sys

def check(f1, f2):
	line = 0

	while(line < len(f1)):
		
		if(f1[line] != f2[line]):
			print("Output not matched on line " + str(line + 1))
			print("your output : " + str(f1[line]) + "actual output : " + str(f2[line]))
			return
		line += 1

	print("Output matched")

def comp(usr_output, sample_output):
	f1 = open(usr_output, 'r').readlines()
	f2 = open(sample_output, 'r').readlines()

	check(f1, f2)