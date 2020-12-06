
def divisibleSumPairs(n, k, ar):
    """
    Determines the number of (i,j) pairs where i < j and 
    ar[i] + ar[j] is divisible by k.

    Parameters:
    n (integer): The length of list ar.
    k (integer): The integer to divide the pair sum by.
    ar (list): A list of integers.

    Returns:
    integer: The number of pairs that meet the requirements.
    """
    pairs = 0
    for i in range(n):
        for j in range(i+1,n):
            if (ar[i]+ar[j])%k == 0: pairs += 1
    return pairs

n, k = list(map(int, input().split()))
ar = list(map(int, input().split()))

print(divisibleSumPairs(n, k, ar))
