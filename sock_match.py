
def sockMerchant(n, ar):
    """
    Determines the number of pairs of socks with matching colors, given 
    a list of integers representing the color of each sock.

    Parameters:
    n (integer): An integer denoting the number of socks in the pile.
    ar (list): A list of integers denoting the colors of each sock.

    Returns:
    integer: An integer denoting the number of matching pairs.
    """
    pairs = 0
    sock_dict = dict.fromkeys(set(ar), 0)   # initialize dict with colors
    for sock in ar: sock_dict[sock] += 1    # find number of socks per color
    for value in sock_dict.values(): pairs += (value//2) # find pairs

    return pairs

n = int(input())
ar = list(map(int, input().split()))
print(sockMerchant(n,ar))