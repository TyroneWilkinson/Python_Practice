#!/bin/python3

import os
import sys

def timeConversion(s):
	"""
	Converts time in 12-hour AM/PM format to military (24-hour) time.
	
	Parameter:
	s (string):	A string representing time in 12-hour format. 
							i.e. hh:mm:ssAM or hh:mm:ssPM
							
	Return:
	string:	A string representing time in 24-hour format.
					i.e. hh:mm:ss
	"""
	if s[-2:] == 'AM':
		if s[0:2] == '12':
			return '00'+ s[2:8]
		return s[0:8]
		
	else:
		if s[0:2] == '12':
			return s[0:8]
		return format(12 + int(s[0:2]), '02.0f') + s[2:8]
	
	
if __name__ == '__main__':
	f = open(os.environ['OUTPUT_PATH'], 'w')

	s = input()

	result = timeConversion(s)

	f.write(result + '\n')

	f.close()
