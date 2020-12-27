# https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=arrays

def rotLeft(a, d):
    """
    Given list a and a number d, perform d left rotations on the list.

    Parameters:
    a (list): An integer list.
    d (integer): The number of left rotations to perform.

    Returns:
    list: List a rotated left d times.
    """
    return a[d:]+a[:d]

n, d = map(int, input().split()) # size of a and # of left rotations
a = list(map(int, input().split()))
print(rotLeft(a, d))