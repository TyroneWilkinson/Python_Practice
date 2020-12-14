# https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem
# Fast enough :)
# Two quick ways of solving this problem:
# 1. Revising the bisect.bisect_left algorithm.
# 2. Use the bisect.bisect_right algorithm with the length of the leaderboard.

# Overwrite above definitions with a fast C implementation
# import bisect
# try:
#     from _bisect import *
# except ImportError:
#     pass

def bleft(a, x, lo=0, hi=None):
    """
    Return the index where to insert item x in list a, assuming a is 
    sorted from largest to smallest.

    The return value i is such that all e in a[:i] have e < x, and all e in
    a[i:] have e >= x.  So if x already appears in the list, a.insert(x) will
    insert just before the leftmost x already there.

    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if a[mid] > x: lo = mid+1
        else: hi = mid
    return lo
    
def climbingLeaderboard(l,p):
    """
    Determine a player's ranking after each game played given his scores
    and the leaderboard scores.

    Note: The game uses dense ranking.

    Parameters:
    l (list): An integer list representing the leaderboard scores.
    p (list): An integer list representing the player's scores.
    
    Returns:
    list: An integer list representing the player's ranking after each score.
    """
    a = sorted(set(l),reverse=True)
    # b = sorted(set(l))
    # n = length(b)
    # print([n-bisect.bisect_right(b,i)-1 for i in p])
    return ([bleft(a,i)+1 for i in p])

input() 
leaderboard = [int(x) for x in input().split()]
input()
player = [int(x) for x in input().split()]
climbingLeaderboard(leaderboard,player)