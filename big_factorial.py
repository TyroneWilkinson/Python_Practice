
# def extraLongFactorials(n):
#     """
#     Calculates then returns the factorial of numbers larger than 20.

#     Parameter:
#     n (integer): The number to find the factorial of.

#     Return:
#     integer: n!
#     """
#     return 1 if n==1 else n*extraLongFactorials(n-1)
# print(extraLongFactorials(int(input())))
from functools import reduce

def extraLongFactorials(n):
    """
    Calculates then prints the factorial of numbers larger than 20.

    Parameter:
    n (integer): The number to find the factorial of.

    Return:
    prints n!
    """
    # for i in range(1,n):
    #     n *= i
    # print(n)
    print(reduce(lambda a,b: a*b, range(1,n+1)))
extraLongFactorials(int(input()))