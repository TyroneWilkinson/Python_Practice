# https://www.hackerrank.com/challenges/utopian-tree/problem
def utopianTree(n):
    """
    Determine how high a utopian tree has grown.
    
    It goes through 2 cycles of growth every year.
    1) Spring: doubles in height.
    2) Summer: increases by 1 meter.
    It starts at 1 meter tall.

    Parameters:
    n (integer): The number of growth cycles the tree has undergone.

    Returns:
    integer: The height of the tree after n growth cycles.
    """
    i = tree = 0
    while i < n+1:
        if i % 2 == 0:
            tree += 1
        else:
            tree *= 2
        i += 1
    return(tree)

t = int(input())
for _ in range(t):
    print(utopianTree(int(input())))