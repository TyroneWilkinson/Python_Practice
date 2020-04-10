#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
	"""
	Determines whether apples and oranges will fall onto a house.
	
	Given the length and location of the house, the location of the 
	apple and orange trees, and where the fruit will fall, we determine
	which fruit will fall on the house.
	
	Parameters:
	s (integer): The starting point of Sam's house location.
	t (integer): The ending location of Sam's house location.
	a (integer): The location of the apple tree.
	b (integer): The location of orange tree.
	apples (list): A list of integers denoting the distances at which
		each apple falls from the tree.
	oranges (list): A list of integers denoting the distances at which
		each orange falls from the tree.	
		
	Return:
	N/A
	Function prints two integers on different lines. The first integer
	is the number of apples that will fall on Sam's house. The second 
	integer is the number of oranges.
	"""
	a_count = o_count = 0
	for x in apples:
		if x + a >= s and x + a <= t:
			a_count += 1
	for y in oranges:
		if y + b >= s and y + b <= t:
			o_count += 1
	
	print(f"{a_count}\n{o_count}")

if __name__ == '__main__':
	st = input().split()

	s = int(st[0])

	t = int(st[1])

	ab = input().split()

	a = int(ab[0])

	b = int(ab[1])

	mn = input().split()

	m = int(mn[0])

	n = int(mn[1])

	apples = list(map(int, input().rstrip().split()))

	oranges = list(map(int, input().rstrip().split()))

	countApplesAndOranges(s, t, a, b, apples, oranges)
