#!/bin/python3

import math
import os
import random
import re
import sys

def staircase(n):
	"""
	Prints a right-aligned staircase of size n using # symbols and spaces.
	
	Parameter:
	n (integer): Denotes the size of the staircase.	
	"""
	i = 1
	while i < n+1:
		print(("#"*i).rjust(n))
		i += 1

if __name__ == '__main__':
	n = int(input())
	
	staircase(n)
