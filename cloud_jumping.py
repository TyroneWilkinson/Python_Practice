# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
def jumpingOnClouds(c):
    """
    Determines the minimum number of jumps it will take to jump from the
    starting postion to the last cloud. The clouds are represented by a 
    list of 0s and 1s where the 1s must be avoided. At most 1 index can 
    be skipped in each jumped.

    Parameters:
    c (list): A list of integers (0s and 1s) denoting clouds.

    Returns:
    integer: The minimum number of jumps required.
    """
    # ones = [i for i,x in enumerate(c) if x==1]
    num_of_clouds = len(c)
    i = jumps = 0
    # while i < num_of_clouds-1:
    #     if i+2 not in ones:
    #         i+=2
    #         jumps+=1
    #     else:
    #         i+=1
    #         jumps+=1
    while i < num_of_clouds-1:
        i += (c[i+2]==0) + 1
        jumps += 1
    return jumps 

input()
c = [int(x) for x in input().split()]
print(jumpingOnClouds(c))