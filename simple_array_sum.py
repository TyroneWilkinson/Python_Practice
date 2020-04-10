#!/bin/python3

import os
import sys

def simpleArraySum(ar):
    """
    Finds the sum of the array's elements.

		Parameters:
		ar (list): A list of integers.

		Returns:
		int: The sum of elements in list ar.
    """

    return sum(ar)
    

if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	ar_count = int(input())

	ar = list(map(int, input().rstrip().split()))

	result = simpleArraySum(ar)

	fptr.write(str(result) + '\n')

	fptr.close()
