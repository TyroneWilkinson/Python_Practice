# A simpler solution...
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
    # pairs = 0
    # for sock in set(ar):
    #     pairs += ar.count(sock)//2

    # return pairs
    return sum([ar.count(sock)//2 for sock in set(ar)])

n = int(input())
ar = list(map(int, input().split()))
print(sockMerchant(n,ar))