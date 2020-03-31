#!/bin/python3

import math
import os
import random
import re
import sys

def plusMinus(arr):
	"""
	Calculates the fractions of an array's elements that are
	positive, negative, and zeros.
	
	Parameter:
	arr (list): A list of integers.
	
	Returns:
	3 integers: A decimal representing the fraction of positive numbers
							in the list.
							A decimal representing the fraction of negative numbers
							in the list.
							A decimal representing the fraction of zeros in the list.
	"""
	
	list_len = len(arr)
	pos = neg = zer = 0
	for x in arr:
		if x > 0:
			pos += 1
		elif x < 0:
			neg += 1
		else:
			zer += 1
	
	return print(("{:6f}\n{:6f}\n{:6f}").format(pos/list_len, 
				 neg/list_len, zer/list_len))

if __name__ == '__main__':
	n = int(input())

	arr = list(map(int, input().rstrip().split()))

	plusMinus(arr)
