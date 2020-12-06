from statistics import multimode

def migratoryBirds(arr):
    """
    Determines the lowest, most frequent number.

    Parameters:
    arr (list): A list of integers.
    
    Returns:
    integer: The minimum mode.
    """
    return min(multimode(arr))

    # Another solution:
    # from collections import Counter
    # return Counter(sorted(arr)).most_common(1)[0][0]

n = int(input())
arr = list(map(int, input().split()))
print(migratoryBirds(arr))