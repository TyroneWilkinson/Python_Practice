#!/bin/python3

import math
import os
import random
import re
import sys

def miniMaxSum(arr):
	"""
	Determines the minimum and maximum values that can be calculated 
	by summing exactly four of the five integers.
	
	Paremeter:
	arr (list): A list of 5 integers.
	
	Return:
	N/A; the respective minimum and maximum values are printed as a 
	single line of two space-separated integers. 
	"""
	arr.sort()
	arr_len = len(arr)
	
	return print(sum(arr[0:arr_len-1]), sum(arr[1:arr_len]))
	

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
