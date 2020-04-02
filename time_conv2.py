#!/bin/python3

import os
import sys

def timeConversion2(s):
	"""
	Converts time in 12-hour AM/PM format to military (24-hour) time.
	
	Parameter:
	s (string):	A string representing time in 12-hour format. 
							i.e. hh:mm:ssAM or hh:mm:ssPM
							
	Return:
	string:	A string representing time in 24-hour format.
					i.e. hh:mm:ss
	"""
	hh, mm, ss = map(int, s[0:8].split(':'))
	tme = s[-2:]
	
	if (tme == "PM") and hh != 12: hh += 12
	if (tme == "AM") and hh == 12: hh = 0
	print("%02d:%02d:%02d" % (hh, mm, ss))

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion2(s)

    f.write(result + '\n')

    f.close()
