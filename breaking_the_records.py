# #!/bin/python3

# import math
# import os
# import random
# import re
# import sys

def breakingRecords(scores):
    """
    Determines the number of times a record is broken for most and least 
    points scored during a season.

    Parameters:
    scores (list): A list of integers representing the points scored in 
        one season.

    Returns:
    integers: Two integers denoting the number of times the max and min 
        points records were broken.
    """

    def comparison(nums, num):
        """
        Compares an integer with all the values in a list of integers.

        Parameters:
        nums (list): List of integers.
        num (integer): An integer.

        Returns:
        integer: A value based on whether num is greater than, less than,
            or neither, when compared to every number in nums.
        """
        return 1 if num > max(nums) else -1 if num < min(nums) else 0

    reviewed = [scores.pop(0)]
    high, low = 0, 0

    for score in scores:        
        check = comparison(reviewed,score)
        if check > 0: high += 1
        if check < 0: low += 1
        reviewed.append(score)

    return high, low

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input())

#     scores = list(map(int, input().rstrip().split()))

#     result = breakingRecords(scores)

#     fptr.write(' '.join(map(str, result)))
#     fptr.write('\n')

#     fptr.close()
