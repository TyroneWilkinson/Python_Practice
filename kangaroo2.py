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
	
	"""
	well, I think it is much easier than we think... We just need solve equation : x1 + y * v1 = x2 + y * v2 where "y" is number of jumps... so if (x1 - x2) % (v2 - v1) == 0 then our kangaroos will meet each other : )
	
	"""
	# To avoid divde by zero 
	if v1 == v2 and x1 == x2:
		return "YES"
	if v1 == v2 and x1 != x2:
		return "NO"
	
	# Equation: x1 + j * v1 = x2 + j * v2 where 'j' is number of jumps.
	jumps = (x2-x1)/(v1-v2)
	return "YES" if jumps > -1 and jumps.is_integer() else "NO"


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
