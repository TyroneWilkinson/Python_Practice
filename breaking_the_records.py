#!/bin/python3
import os

def getTotalX(a, b):
    """
    Finds the integers that are "between" two given lists.
    Determines which integers meets two requirements:
    1. All the numbers in list a are its factors.
    2. It is a factor of all the numbers in list b.

    Parameters:
    a (list): A list of integers.
    b (list): A list of integers.

    Returns:
    int: The number of integers that meet the requirments.
    """
    a_set, b_set = set(), set()
    a_list, b_list = [], []
    low = max(a)
    high = min(b)

    for i in list(range(low,high+1)):
        for j in a:
            if not i%j: a_list.append(i)
        if len(a_list)==len(a): a_set.add(i)
        a_list = []
        for k in b:
            if not k%i: b_list.append(i)
        if len(b_list)==len(b): b_set.add(i)
        b_list = []

    return len(a_set.intersection(b_set))

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     first_multiple_input = input().rstrip().split()

#     n = int(first_multiple_input[0])

#     m = int(first_multiple_input[1])

#     arr = list(map(int, input().rstrip().split()))

#     brr = list(map(int, input().rstrip().split()))

#     total = getTotalX(arr, brr)

#     fptr.write(str(total) + '\n')

#     fptr.close()
