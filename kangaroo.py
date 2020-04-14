#!/bin/python3

import math
import os
import random
import re
import sys

def kangaroo(x1, v1, x2, v2):
	"""
	Determines whether 2 kangaroos ever jump on the same spot 
	simultaneously given their starting positions and jump distance.
	
	Parameters:
	x1 (integer): The starting position for kangaroo 1.
	v1 (integer): The jump distance for kangaroo 1.
	x2 (integer): The starting position for kangaroo 2.
	v2 (integer): The jump distance for kangaroo 2. 
	
	Returns:
	string: "YES" if the kangaroos ever land on the same location at the
	same time; otherise, print "NO".
	"""
	# If the distance between kangaroos increase then they'll never meet.
	diff1 = abs(x1 - x2)
	while(True):
		x1 += v1
		x2 += v2
		diff2 = abs(x1 - x2)
		if diff2 >= diff1:
			return "NO"
		if diff2 == 0:
			return "YES"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
