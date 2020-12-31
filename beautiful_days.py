# https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem

def beautifulDays(i,j,k):
    """
    Given a range of numbered days and a number, determine the number of
    days in the range that are beautiful. 
    Beautiful days are defined as numbers where |i - reverse(i)| is evenly
    divisible by k.
    
    Parameters:
    i (int): The starting day number.
    j (int): The ending day number.
    k (int): The divisor.

    Returns:
    int: The number of beautiful days in the range.    
    """
    return sum([1 for x in range(i,j+1) if abs(x-int(str(x)[::-1])) % k == 0])

print(beautifulDays(*map(int, input().split())))