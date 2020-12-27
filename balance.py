# https://www.hackerrank.com/challenges/balanced-brackets/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=stacks-queues

def isBalanced(s):
    """
    Determines whether a string containing 3 types of brackets is balanced.

    A sequence of brackets is balanced if:
    -It contains no unmatched brackets.
    -The subset of brackets enclosed within the confines of an matched pair
     of brackets is also an matched pair of brackets.
    
    Parameters:
    s (string): A string of brackets.

    Returns:
    string: "YES" if the sequence is balanced or "NO" if it is not.
    """
    if len(s)%2 != 0: return "NO"

    bracket_dict = {'{':'}', '[':']', '(':')'}
    bracket_lst = []
    i = 0

    if s[0] not in bracket_dict: return "NO"

    for bracket in s:
        if bracket in bracket_dict:
            bracket_lst.insert(0,bracket_dict[bracket])
            i+=1
        else:
            try:
                if bracket != bracket_lst.pop(0):
                    return "NO"
            except IndexError:
                return "NO"
    
    return "YES" if bracket_lst == [] else "NO"

n = int(input()) # The number of strings
with open('temp.txt', 'w+') as f:
    for _ in range(n):
        s = input().strip()
        print(isBalanced(s))


# n = int(input()) # The number of strings
# with open('temp.txt', 'w+') as f:
#     for _ in range(n):
#         s = input().strip()
#         f.write(isBalanced(s))
#         f.write('\n')

# with open('temp0.txt') as f1, open('temp.txt') as f2:
#     for i, (line1, line2) in enumerate(zip(f1,f2),1):
#         if line1!=line2:
#             print(f'Line number {i}: {line1} != {line2}')
