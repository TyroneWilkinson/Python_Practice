def birthday(s, d, m):
    """
    Determines the number of ways a list of integers can be divided given
    the following requirements:
    A contiguous segment must be (1) m-integers long and (2) add up to d.

    Parameters:
    s (list): A list of integers.
    d (integer): An integer denoting what the sum of the segment must be.
    m (integer): An integer denoting how long the segment must be.

    Returns:
    integer: The number of ways the list can be segmented.
    """
    segments = 0
    # The "+1-m" is to ensure that the correct segment lengths are summed.
    for i in range(len(s)+1-m): 
        if sum(s[i:i+m]) == d: segments += 1
    return segments


n = int(input())
s = list(map(int, input().split()))
d, m = map(int, input().split())
print(birthday(s, d, m))