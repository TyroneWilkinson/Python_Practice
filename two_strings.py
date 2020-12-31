# https://www.hackerrank.com/challenges/two-strings/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=dictionaries-hashmaps

def twoStrings(s1, s2):
    """
    Determines whether two strings share a common substring.

    Parameters:
    s1 (string):
    s2 (string):

    Returns:
    string: "YES" or "NO" if there is a common substring or not.
    """
    return "YES" if set(s1).intersection(set(s2)) else "NO"
    # return "YES" if set(s1) & set(s2) else "NO"

p = int(input()) # Number of test cases.
for _ in range(p):
    s1 = input().strip()
    s2 = input().strip()
    print(twoStrings(s1,s2))