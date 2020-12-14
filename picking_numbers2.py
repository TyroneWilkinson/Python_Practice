#https://www.hackerrank.com/challenges/picking-numbers/problem
# A simpler way of solving this problem.
def pickingNumbers(a):
    """
    Determines the longest sublist where the absolute difference between
    any two elements is less than or equal to 1.

    Parameters:
    a (list): A list of integers.

    Returns:
    integer: The length of the longest sublist.
    """
    # total = 0 
    # for i in a:
    #     x_dups = a.count(i)
    #     y_dups = a.count(i-1)
    #     dups = x_dups + y_dups
    #     if dups > total: total = dups
    # return total
    return max(a.count(i)+a.count(i-1) for i in a)

input()
a = [int(i) for i in input().split()]
print(pickingNumbers(a))