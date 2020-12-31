# https://www.hackerrank.com/challenges/save-the-prisoner/problem

def saveThePrisoner(n,m,s):
    """
    Given m sweets and a circular queue of n prisoners, determine which 
    prisoner will receive the last (bitter) sweet.

    Parameters:
    n (int): The number of prisoners.
    m (int): The number of sweets.
    s (int): The chair number to begin passing out sweets from.

    Returns:
    int: The chair number of the prisoner to warn about the bitter sweet. 
    """
    # First-ish attempt:
    # prisoners = list(range(1,n+1))
    # if m > n: return (prisoners[s-1:]+prisoners[:s-1])[m%n-1] 
    # if m == n: return (prisoners[s-1:]+prisoners[:s-1])[-1]
    # return (prisoners[s-1:]+prisoners[:s-1])[n%m]

    # I had to make note of 4 possible cases, below:
    if n == 1: return 1
    position = ( ( s+m ) % n ) - 1
    if position < 1: return n + position 
    return position


for _ in range(int(input())):
    n,m,s = map(int, input().split())
    print(saveThePrisoner(n,m,s))

# with open('save_prisoner_1.txt', 'w+') as f:
#     for _ in range(int(input())):
#         n,m,s = map(int, input().split())
#         f.write(str(saveThePrisoner(n,m,s)))
#         f.write('\n')

# with open('save_prisoner_0.txt') as f1, open('save_prisoner_1.txt') as f2, \
#      open('save_prisoner_2.txt', 'w+') as f3:
#     for i, (line1, line2) in enumerate(zip(f1,f2),1):
#         if line1!=line2:
#             f3.write(f'Line number {i}: {line1} != {line2}')
#             f3.write('\n')
