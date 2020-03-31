#!/bin/python3

import math
import os
import random
import re
import sys

def diagonalDifference(arr):
  """
  Finds the absolute difference between the sum of the diagonals in a 
	square matrix.
	
	Parameter:
	arr (list): A 2D list of integers.
	
	Returns:
	integer: The "diagonal difference."
  """
	
  i_by_i = len(arr)
  l_to_r_diagonal = arr[:]
  l_to_r_sum = 0
	
	arr.reverse()
  r_to_l_diagonal = arr
  r_to_l_sum = 0
  
  for i in range(i_by_i):
    l_to_r_sum += l_to_r_diagonal[i][i]
    r_to_l_sum += r_to_l_diagonal[i][i]

  return abs(l_to_r_sum - r_to_l_sum)
  
if __name__ == '__main__':
  fptr = open(os.environ['OUTPUT_PATH'], 'w')

  n = int(input().strip())

  arr = []

  for _ in range(n):
      arr.append(list(map(int, input().rstrip().split())))

  result = diagonalDifference(arr)

  fptr.write(str(result) + '\n')

  fptr.close()
