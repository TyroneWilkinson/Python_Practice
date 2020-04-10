#!/bin/python3

import math
import os
import random
import re
import sys

def aVeryBigSum(ar):
	"""
	Finds the sum of the array's elements.
	
	Note: 
	There are no "long" data types in Python so the sum function
	is sufficient for large numbers.

	Parameters:
	ar (list): A ist of integers.

	Returns:
	int: The sum of elements in list ar.
	"""

	return sum(ar)

if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	ar_count = int(input())

	ar = list(map(int, input().rstrip().split()))

	result = aVeryBigSum(ar)

	fptr.write(str(result) + '\n')

	fptr.close()
