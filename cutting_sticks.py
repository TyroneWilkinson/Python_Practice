#!/bin/python3

import math
import os
import random
import re
import sys

def cutTheSticks(arr):
	"""
	A function that iteratively cuts a series of sticks into smaller sticks
	until there are none remaining. The number of sticks at each iteration 
	in which sticks are removed is returned.
	
	Parameter:
	arr (list): A list of integers representing the length of each stick.

	Return:
	list: A list of integers that represent the number of sticks cut at 
	each iteration in which sticks are removed.	
	"""
	cut_sticks = []
	arr_len = len(arr)
	cut_sticks.append(arr_len)
	while (len(arr)):
		arr = list(map(lambda x: x - 1, arr))
		arr = list(filter(lambda x: x > 0, arr))
		if not(arr_len == len(arr)):
			arr_len = len(arr)
			cut_sticks.append(arr_len)
	
	return cut_sticks[0:-1]
		
if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	n = int(input())

	arr = list(map(int, input().rstrip().split()))

	result = cutTheSticks(arr)

	fptr.write('\n'.join(map(str, result)))
	fptr.write('\n')

	fptr.close()
