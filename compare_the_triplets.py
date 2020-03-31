#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
	"""
	Compares two triplets and awards points depending on the values.

	If a[i] > b[i], then Player A gets a point.
	If a[i] < b[i], then Player B gets a point. 
	If a[i] = b[i], then neither player gets a point. 

	Parameters:
	a (list): List of 3 integers
	b (list): List of 3 integers.

	Returns:
	list: A list of 2 integers containing Player A's points first and
				Player B's points second.
	"""

	i = playerA = playerB = 0

	while i < len(a):
		if a[i] > b[i]:
			playerA += 1
		elif a[i] < b[i]:
			playerB += 1
		else:
			pass
		i += 1

	return [playerA, playerB]

if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	a = list(map(int, input().rstrip().split()))

	b = list(map(int, input().rstrip().split()))

	result = compareTriplets(a, b)

	fptr.write(' '.join(map(str, result)))
	fptr.write('\n')

	fptr.close()
