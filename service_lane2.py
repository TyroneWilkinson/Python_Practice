#!/bin/python3

import math
import os
import random
import re
import sys

def serviceLane(cases, width):
	"""
	Calulates the minimum value in a specified segment of a list.

	Parameters:
	cases (list): A 2-D list of integers where each element is a list of 
		2 integers representing starting and ending indices for a segment 
		of the 'width' list.
	width (list): A list of integers that will be segmented
	
	Return:
	list: A list of integers with each int representing the minimum value
		in the given segment.
	"""
	return [min(width[segment[0]:segment[1]+1]) for segment in cases]	

if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	nt = input().split()

	n = int(nt[0])

	t = int(nt[1])

	width = list(map(int, input().rstrip().split()))

	cases = []

	for _ in range(t):
		cases.append(list(map(int, input().rstrip().split())))

	result = serviceLane(cases, width)

	fptr.write('\n'.join(map(str, result)))
	fptr.write('\n')

	fptr.close()
