# https://www.hackerrank.com/challenges/ctci-ransom-note/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
from collections import Counter
def checkMagazine(magazine, note):
    """
    Given two sets of dictionaries (lists of strings), tell if one of them
    is a subset of the other. Check if the note can be formed using the
    magazine. The words are case-sensitive.

    Parameters:
    magazine (list): A list of strings, each a word in the magazine.
    note (list): A list of strings, each a word in the ransom note.

    Returns:
    string: "Yes" if the note is a subset of the magazine, else "No."
    """
    # m = Counter(magazine)
    # n = Counter(note)
    # for word in set(note):
    #     if m[word] < n[word]:
    #         return print("No")
    # return print("Yes")

    # When an empty dict is returned, every element in note is present 
    # enough times in magazine, else a dictionary with those pairs are 
    # returned.
    return "Yes" if Counter(note)-Counter(magazine)=={} else "No"

m, n = [int(x) for x in input().split()]
magazine = [x for x in input().split()]
note = [x for x in input().split()]
checkMagazine(magazine,note)
