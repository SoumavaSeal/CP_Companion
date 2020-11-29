import sys
import os
import compare

prblm = sys.argv[1]

loc = "./sample-test/" + prblm + "/inputs"

testcaseses = [name for name in os.listdir(loc)]

i = 1

print("compiling....")
os.system("g++ " + prblm + ".cpp")
print("compiling finished!")

for test in testcaseses:
	text = "a.exe < ./sample-test/" + prblm + "/inputs/" + test + " > " + prblm + ".txt"

	usr_loc = prblm + ".txt"
	sample_loc = "./sample-test/" + prblm + "/outputs/" + test

	os.system(text)
	
	print("Running Testcase " + str(i))
	i += 1
	compare.comp(usr_loc, sample_loc)