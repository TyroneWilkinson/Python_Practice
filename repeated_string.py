def repeatedString(s,n):
    """
    Determines the amount of times the letter 'a' appears in a repeated 
    subsstring, given the number of characters to consider.

    Parameters:
    s (string): The string to be repeated.
    n (integer): The number of characters to consider.

    Returns:
    integer: The frequency of a in the substring.   
    """
    # s_len = len(s)
    # main = n // s_len
    # remain = n % s_len
    # main_freq = len([i for i,chr in enumerate(s) if chr=="a"])*main
    # remain_freq = len([i for i,chr in enumerate(s[:remain]) if chr=="a"])
    # return main_freq+remain_freq
    return s.count("a")* (n // len(s)) + s[:n % len(s)].count("a")

s = input().strip()
n = int(input())

print(repeatedString(s,n))