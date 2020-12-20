# https://www.hackerrank.com/challenges/ctci-making-anagrams/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=strings
from collections import Counter
def makeAnagram(a, b):
    """
    Determines the minimum number of characters to delete to make two
    strings anagrams of each other.

    Parameters:
    a (string): A string to compare to string b.
    b (string): A string to compare to string a.

    Returns:
    integer: The minimum total characters that must be deleted.
    """
    aa = Counter(a)
    bb = Counter(b)
    aa.subtract(bb)
    return sum([abs(i) for i in aa.values()])

a = input().strip()
b = input().strip()
print(makeAnagram(a,b))