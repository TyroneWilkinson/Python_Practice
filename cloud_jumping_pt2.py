# https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem

def jumpingOnClouds(c, k):
    """
    Determine the amount of energy a character has after the cloud game
    ends. 
    You start with 100 energy. Every jump uses 1 energy unit. Landing on a 
    thundercloud (1) uses an additional 2 energy units. The game ends when 
    the player lands back on cloud 0.

    Note: Each jump of size k lands you to cloud c[(i+k)%n].

    Parameters:
    c (list): The cloud types along the path (0,1).
    k (int): The length of one jump.
    
    Returns:
    int: The energy level remaining.
    """
    # First answer:
    # i = jumps = 0
    # n = len(c)
    # while True:
    #     jumps += 1
    #     i = (i+k)%n
    #     if c[i] == 1:
    #         jumps += 2
    #     if i == 0:
    #         return 100 - jumps

    # Second answer:
    # def lcm(x,y):
    #     """
    #     Find the least common multiple by using the greatest common divisor.
    #     Python 3.9+ has a lcm function in the math library.
    #     """
    #     try:
    #         from math import lcm
    #         return lcm(x,y)
    #     except ImportError:
    #         from math import gcd
    #         return (x*y) // gcd(x,y)
    #
    # all_jumps = jumps = lcm(len(c),k)//k
    #
    # n = len(c)
    # i = 0
    # for _ in range(jumps):
    #     i = (i+k)%n
    #     if c[i] == 1:
    #         all_jumps += 2
    # return 100 - all_jumps

    # Best answer (which I found):
    energy = 100 #initial energy
    i = k % n #initial jump from 0
    energy -= c[i] * 2 + 1 #initial energy loss
    while i != 0:
        i = (i + k) % n
        energy -= c[i] * 2 + 1
    return energy


n, k = map(int, input().split()) # Number of clouds and the jump distance
c = [int(x) for x in input().split()]
print(jumpingOnClouds(c,k))

