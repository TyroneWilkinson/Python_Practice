# https://www.hackerrank.com/challenges/find-digits/problem
def findDigits(n):
    """
    Given an integer, for each digit that makes up the integer determine 
    whether it is a divisor.

    Parameters:
    n (int): The integer to analyze.

    Returns:
    integer: The number of digits in n that are divisors of n.
    """
    return sum([1 for i in str(n) if int(i) > 0 and n%int(i) == 0])

for _ in range(int(input())):
    print(findDigits(int(input())))
