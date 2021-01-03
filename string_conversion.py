# https://www.hackerrank.com/challenges/append-and-delete/problem

def appendAndDelete(s,t,k):
    """
    Determines whether string s can be converted to string t in exactly k 
    operations.
    Two operations can be performed: 
    1) Appending to the end of the string.
    2) Deletion of the last character of a string.

    Parameters:
    s (string): The initial string.
    t (string): The desired string.
    k (int): The exact number of operations that must be performed.

    Returns:
    string: "Yes" or "No" if string s can be converted in k operations.
    """
    len_s = len(s)
    len_t = len(t)
    matches = 0
    for i in range(len_s if len_s < len_t else len_t):
        if s[i] == t[i]:
            matches += 1
        else:
            break
    operations = (len_s - matches) + (len_t - matches) 

    # There are 3 cases in which string s can be converted to string t:
    # 1. The number of operations
    # 2. The number of operations + 2 into infinity.
    # 3. All numbers >= len(s) + len(b)
    #    This is because any number of operations can occur to an empty string.
    # Note: I combined case 1 and 2 below.
    if (k % 2 == operations % 2 and k >= operations) or k > len_s + len_t:
        return "Yes"
    return "No"

s = input().strip()
t = input().strip()
k = int(input())

print(appendAndDelete(s,t,k))