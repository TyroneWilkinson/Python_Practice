#!/bin/python3

import math
import os
import random
import re
import sys

def workbook(n, k, arr):
	"""
	Determines the number of "special" problems in a given workbook.
	
	A special problem is one in which the problem number for that 
	particular chapter matches the page number in the workbook.
	
	Parameters:
	n (integer): The number of chapters in the workbook.
	k (integer): The maximum number of problems per page.
	arr (list): A list of integers that denote the number of problems
		in each chapter. 
	
	Return:
	integer: The number of special problems in Lisa's workbook.
	"""
	max_probs = k
	pgs = specials = 0
	for i, probs in enumerate(arr):
		new_pgs = 0
		chapters = i + 1 # Didn't use--don't need 'enumerate' method.
		full_pgs = math.floor(probs/max_probs)
		overflow = probs%max_probs
		
		# Checks whether pg number matches a problem number on that full pg
		for i in range(full_pgs):
			pgs += 1
			new_pgs = i + 1
			current_probs = new_pgs * max_probs
			if pgs in [x for x in range(((new_pgs-1)*max_probs)+1, current_probs+1)]:
				specials += 1
		# Checks whether pg number matches a problem number on that full pg
		if overflow:
			pgs += 1
			new_pgs = new_pgs + 1 if full_pgs else 1 # continues pgs or starts fresh
			current_probs = (new_pgs - 1) * max_probs
			if pgs in [x for x in range(current_probs+1, current_probs+overflow+1)]:
				specials += 1
	
	return specials

if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	nk = input().split()

	n = int(nk[0])

	k = int(nk[1])

	arr = list(map(int, input().rstrip().split()))

	result = workbook(n, k, arr)

	fptr.write(str(result) + '\n')

	fptr.close()
