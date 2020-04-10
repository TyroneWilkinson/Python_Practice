#!/bin/python3

import math
import os
import random
import re
import sys

def chocolateFeast(n, c, m):
	"""
	Determines the number of chocolates Bobby can eat.
	
	Rules:
	- Chocolate bars cost c cents each.
	- m wrappers can be traded in for 1 chocolate bar.
	
	Parameters:
	n (int): An integer representing Bobby's initial amount of money.
	c (int): An integer representing the cost of a chocolate bar.
	m (int): An integer representing the number of wrappers Bobby can 
					 turn in for a free bar.
					 
	Return:
	integer: The total number of chocolates Bobby eats.
	"""
	# wrappers: w
	# bars : b
	b = w = math.floor(n/c)
	while w >= m:
		b_from_w = math.floor(w/m)
		b += b_from_w
		w = w - (b_from_w * m) + b_from_w
	
	return b
	
if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	t = int(input())

	for t_itr in range(t):
		ncm = input().split()

		n = int(ncm[0])

		c = int(ncm[1])

		m = int(ncm[2])

        result = chocolateFeast(n, c, m)

        fptr.write(str(result) + '\n')

    fptr.close()
