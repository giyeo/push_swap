from itertools import permutations
import random
import os

def do_test_with(number, times, mode):
	for one in range(times):
		if(mode == 1):
			hundred = permutations(range(number), number)
			for each in hundred:
				string = "./pushswap "
				for one in each:
					string+=str(one) + " "
				os.system(string)
		else:
			hundred = random.sample(range(number), number)
			string = "./pushswap "
			for each in hundred:
				string+=str(each) + " "
			os.system(string)

#	1 for permutations, 0 to random numbers
do_test_with(100, 50, 0)