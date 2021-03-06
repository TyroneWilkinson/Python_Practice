#!/bin/python3

import math
import os
import random
import re
import sys

def gradingStudents2(grades):
	"""
	Determines a student's grades according to a grading policy.
	
	Grading Policy:
	- A grade is between 0 and 100 inclusively.
	- A grade < 40 is failing.
	- If the difference between the grade and the next multiple of 
		5 is < 3, round grade up to the next multiple of 5. 
	- No rounding occurs if grade < 38. 
	
	Parameter:
	grades (list): A list of integers representing grades before rounding.
	
	Return:
	list: A list of integers representing the student's new grades.
	"""
	rgrades = []
	for x in grades:
		rgrades.append(x) if (x < 38 or x % 5 < 3) else rgrades.append(x + (5-(x%5)))
	return rgrades
		
if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')

	grades_count = int(input().strip())

	grades = []

	for _ in range(grades_count):
			grades_item = int(input().strip())
			grades.append(grades_item)

	result = gradingStudents(grades)

	fptr.write('\n'.join(map(str, result)))
	fptr.write('\n')

	fptr.close()
