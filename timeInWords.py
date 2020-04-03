#!/bin/python3

import math
import os
import random
import re
import sys

def timeInWords(h, m):
	"""
	Converts a given time from numerals into words.
	
	-At minutes = 0, "o' clock" is used. E.g. five o'clock.
	-For 1 <= minutes <= 30, "past" is used. E.g. ten minutes past five.
	-For 30 < minutes, "to" is used. E.g. ten minutes to five.
	Note: 
	The word "quarter" will replace "fifteen minutes."
	The word "half" will replace "thirty minutes."
	E.g. quarter past five.
	E.g. half past five.
		
	Parameters:
	h (integer): An integer representing hour of the day.
	m (integer): An integer representing minutes after the hour.
	
	Return:
	string: The time in words.
	"""
	
	# numToWord returns a string for a given integer.
	def numToWord(x):
		numbers = ["","one ","two ","three ","four ","five ","six ", \
		"seven ","eight ","nine ","ten ","eleven ","twelve ","thirteen ", \
		"fourteen ","fifteen ","sixteen ","seventeen ","eighteen ", \
		"nineteen ","twenty ","twenty one ","twenty two ", "twenty three ", \
		"twenty four ","twenty five ","twenty six ","twenty seven ", \
		"twenty eight ","twenty nine ", "thirty "]
		return numbers[x]
		
	quarter = "quarter "
	half = "half "
	m_word = ["minute ", "minutes "]
	past = "past " 
	to = "to "
	oc_word = "o' clock"
	diff = 30 - m
	
	# There are multiple cases to consider:
	# x o' clock
	# one minute	past/to		h/h+1
	# x minutes 	past/to		h/h+1
	# quarter			past/to		h/h+1
	# half				past			h
	if diff == 30: return(numToWord(h) + oc_word)
	if diff > -1: 
		if diff == 29: return(numToWord(m) + m_word[0] + past + numToWord(h))
		elif diff == 15: return(quarter + past + numToWord(h))
		elif diff == 0: return(half + past + numToWord(h))
		else: return(numToWord(m) + m_word[1] + past + numToWord(h))
	if diff < 0:
		if diff == -29: return(numToWord(diff - 1) + m_word[0] + to + numToWord(h+1))
		elif diff == -15: return(quarter + to + numToWord(h + 1))
		else: return(numToWord(diff - 1) + m_word[1] + to + numToWord(h + 1))
	
"""
 TEST CASES	
	
timeInWords(5, 0)	
timeInWords(5, 1)	
timeInWords(5, 15)	
timeInWords(5, 25)	
timeInWords(5, 30)	
timeInWords(5, 45)	
timeInWords(5, 55)	
timeInWords(5, 59)	
"""	
					
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
