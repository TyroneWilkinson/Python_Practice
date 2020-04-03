# A more readable solution I found.
def timeInWords(h, m):
    hours = {0:"zero", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six",
					 7:"seven", 8:"eight", 9:"nine", 10:"ten", 11:"eleven", 12:"twelve", 
					 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen",
					 18:"eighteen", 19:"nineteen", 20:"twenty", 21:"twenty one", 22:"twenty two",
					 23:"twenty three"}
	minutes = {0:"o' clock", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 
						 7:"seven", 8:"eight", 9:"nine", 10:"ten", 11:"eleven", 12:"twelve", 
						 13:"thirteen", 14:"fourteen", 15:"quarter", 16:"sixteen", 17:"seventeen", 
						 18:"eighteen", 19:"nineteen", 20:"twenty", 21:"twenty one", 
						 22:"twenty two", 23:"twenty three", 24:"twenty four", 25:"twenty five",
						 26:"twenty six", 27:"twenty seven", 28:"twenty eight", 29:"twenty nine",
						 30:"half", 45:"quarter"}
	if (m == 1):
			times = minutes[m] + " minute past " + hours[h]
			return times
	else:
			if (m == 15) or (m == 30):
					times = minutes[m] + " past " + hours[h]
					return times
			elif (m == 45):
					times = minutes[m] + " to " + hours[h+1]
					return times
			elif (m == 0):
					times = hours[h] + " " + minutes[m]
					return times
			else:
					if ((m >= 1) and (m <= 30)):
							times = minutes[m] + " minutes past " + hours[h]
							return times
					else:
							times = minutes[60-m] + " minutes to " + hours[h+1]
							return times