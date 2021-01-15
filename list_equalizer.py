# https://www.hackerrank.com/challenges/equality-in-a-array/problem?isFullScreen=true

def equalizeArray(arr):
    """
    Determines the minimal number of elements to delete from a list
    for all remaining elements to be the same.

    Parameters:
    arr (list): A list of integers.

    Returns:
    integer: The minimum number of deletions required.
    """
    # return sum(sorted([arr.count(i) for i in set(arr)], reverse=True)[1:])
    return len(arr) - max([arr.count(i) for i in arr]) # A better solution
    # return len(arr)-max(collections.Counter(arr).values()) # Apparently O(n)

n = int(input()) # length of arr
arr = list(map(int,input().split()))
print(equalizeArray(arr))