#https://www.hackerrank.com/challenges/picking-numbers/problem
def pickingNumbers(a):
    """
    Determines the longest sublist where the absolute difference between
    any two elements is less than or equal to 1.

    Parameters:
    a (list): A list of integers.

    Returns:
    integer: The length of the longest sublist.
    """
    a = sorted(a)[::-1]
    len_a = len(a)
    counts = []
    for ind, ele in enumerate(a):
        count = 0
        for i in range(ind, len_a):
            if ele - a[i] < 2:
                count += 1
            else:
                break
        counts.append(count)
    return max(counts)

input()
a = list(map(int,input().split()))
print(pickingNumbers(a))