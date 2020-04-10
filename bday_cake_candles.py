#!/bin/python3

import math
import os
import random
import re
import sys

def birthdayCakeCandles(ar):
	"""
	Determines the quantity of the largest integer(s) in the list.
	
	Parameter:
	ar (list): A list of integers representing candle heights.

	Return:
	integer: An integer representing the number of candles that can be
					 blown.	
	"""
	return ar.count(max(ar))

if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	ar_count = int(input())

	ar = list(map(int, input().rstrip().split()))

	result = birthdayCakeCandles(ar)

	fptr.write(str(result) + '\n')

	fptr.close()

