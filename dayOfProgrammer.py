def dayOfProgrammer(year):
    """
    Given a year, determines the date of the 256th day of the year,
    the "Day of the programmer," according to the Russian calendar.
    
    Note:
    From 1700 to 1917 Russia's calendar was the Julian calendar.
    -The leap year was a year divisible by four.
    After 1918 Russia's calendar was the Gregorian calendar.
    -The leap year was a year divided by 400 or 
     (a year divisible by 4 and not divisible by 100).
    1918 was a transitory period from the Julian to the Gregorian calendar.
    -The day after January 31st was February 14th. 
    The 256th day was generally September 12 in leap years and 13 otherwise.

    Constraints:
    Year will be in the inclusive range of 1700 and 2700.
    
    Parameters:
    year (integer): The year we must find the date of.

    Returns:
    string: The date represented in the format dd.mm.yyyy
    """
    def divisible(x,y):
        """
        Tells you whether integer x is divisible by integer y.
        """
        return True if x % y == 0 else False

    if year < 1918:
        return f"12.09.{year}" if divisible(year,4) else f"13.09.{year}"
    elif year > 1918:
        return f"12.09.{year}" if divisible(year,400) or \
                                 (divisible(year,4) and not divisible(year,100)) \
                               else f"13.09.{year}"
    else:
        return "26.09.1918"

print(dayOfProgrammer(int(input().strip())))